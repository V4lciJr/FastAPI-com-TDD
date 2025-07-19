from typing import List, Optional

from fastapi import APIRouter, status, Body, Depends, Path, HTTPException, Query
from pydantic import UUID4

from store.core.execptions import NotFoundException, InsertionException
from store.schemas.product import ProductIn, ProductOut, ProductUpdate
from store.usecases.product import ProductUsecase

router = APIRouter(tags=["products"])


@router.post(
    path="/",
    summary="Create a new product",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductOut,
)
async def post(
    body: ProductIn = Body(...), usecase: ProductUsecase = Depends()
) -> ProductOut:
    try:
        return await usecase.create(body=body)
    except InsertionException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An unexpected error occurred while creating the product: {e}",
        )


@router.get(path="/{id}", summary="get product by id", status_code=status.HTTP_200_OK)
async def get(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> ProductOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as exc:
        raise exc


@router.get(
    path="/",
    summary="query all products",
    status_code=status.HTTP_200_OK,
    response_model=List[ProductOut],
)
async def query(
    usecase: ProductUsecase = Depends(),
    min_price: Optional[float] = Query(None, description="Minimum price for products"),
    max_price: Optional[float] = Query(None, description="Maximum price for products"),
) -> List[ProductOut]:
    return await usecase.query(min_price=min_price, max_price=max_price)


@router.patch(
    path="/{id}", summary="update products by id", status_code=status.HTTP_200_OK
)
async def patch(
    id: UUID4 = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUsecase = Depends(),
) -> ProductOut:
    try:
        return await usecase.update(id=id, body=body)
    except NotFoundException as exc:
        raise exc


@router.delete(
    path="/{id}",
    summary="delete products by id",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise exc
