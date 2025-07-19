from datetime import datetime
from typing import List, Optional
from uuid import UUID

import pymongo
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from pymongo.errors import PyMongoError

from store.db.mongo import db_client
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.core.execptions import NotFoundException, InsertionException


class ProductUsecase:
    def __init__(self):
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())

        try:
            await self.collection.insert_one(product_model.model_dump())
        except PyMongoError as e:
            raise InsertionException(
                message=f"Error inserting product into database: {e}"
            )

        return ProductOut(**product_model.model_dump())

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductOut(**result)

    async def query(
        self, min_price: Optional[float] = None, max_price: Optional[float] = None
    ) -> List[ProductOut]:
        filter_query = {}

        if min_price is not None or max_price is not None:
            price_conditions = {}

            if min_price is not None:
                price_conditions["$gte"] = min_price
            if max_price is not None:
                price_conditions["$lt"] = max_price

            if price_conditions:
                filter_query["price"] = price_conditions

        return [ProductOut(**item) async for item in self.collection.find(filter_query)]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        update_data = body.model_dump(exclude_unset=True)
        if "updated_at" not in update_data:
            update_data["upadated_at"] = datetime.now()

        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": update_data},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        if not result:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(message=f"Product not found with filter: {id}")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False


product_usecase = ProductUsecase()
