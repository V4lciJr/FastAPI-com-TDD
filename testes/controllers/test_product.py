from typing import List

import pytest

from testes.factories import product_data
from fastapi import status


async def test_controller_create_shlould_return_sucess(client, products_url):
    response = await client.post(products_url, json=product_data())

    assert response.status_code == status.HTTP_201_CREATED


async def test_controller_get_shlould_return_sucess(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_200_OK


async def test_controller_get_shlould_return_not_found(client, products_url):
    response = await client.get(f"{products_url}616605e4-f277-4447-ba69-eded993cd33f")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 616605e4-f277-4447-ba69-eded993cd33f"
    }


@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_shlould_return_sucess(client, products_url):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1


async def test_controller_patch_shlould_return_sucess(
    client, products_url, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"quantity": 100}
    )

    assert response.status_code == status.HTTP_200_OK


async def test_controller_delete_shlould_return_no_content(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_shlould_return_not_found(client, products_url):
    response = await client.delete(
        f"{products_url}616605e4-f277-4447-ba69-eded993cd33f"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {
        "detail": "Product not found with filter: 616605e4-f277-4447-ba69-eded993cd33f"
    }
