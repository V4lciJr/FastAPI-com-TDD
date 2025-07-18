from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel, UUID4

from store.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., description="Product name")
    quantity: int = Field(..., description="Product quantity")
    price: float = Field(..., description="Product price")
    status: bool = Field(..., description="Product Status")


class ProductIn(ProductBase, BaseSchemaMixin):
    ...


class ProductOut(ProductIn):
    id: UUID4 = Field()
    created_at: datetime = Field()
    update_at: datetime = Field()


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(None, description="Product quantity")
    price: Optional[float] = Field(None, description="Product price")
    status: Optional[bool] = Field(None, description="Product Status")


class ProductUpdateOut(ProductUpdate):
    ...
