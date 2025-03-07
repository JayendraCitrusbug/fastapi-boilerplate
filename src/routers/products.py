from fastapi import APIRouter

from src.application.products import ProductAppServices
from src.schema.products import (
    CreateProductRequestSchema,
    CreateProductResponseSchema,
    DeleteProductResponseSchema,
    GetProductResponseSchema,
    GetProductsListingsResponseSchema,
    UpdateProductRequestSchema,
    UpdateProductResponseSchema,
)

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("/", response_model=GetProductsListingsResponseSchema)
async def get_all_products():
    """
    Method to get all products.

    Returns:
        List[Product]: A list of all products.
    """
    product_app_services = ProductAppServices()
    await product_app_services.get_products_list()
    # if role == "admin":
    #     return await product_app_services.get_products_list()
    # return await product_app_services.get_products_by_user_id(user_id=role)


@router.get("/{product_id}", response_model=GetProductResponseSchema)
async def get_product_by_id(product_id: str):
    """
    Method to get a product by id.

    Args:
        product_id (str): Product id.

    Returns:
        Product: A Product object.
    """
    product_app_services = ProductAppServices()
    return await product_app_services.get_product_details_by_id(
        product_id=product_id,
        raise_exception=False,
    )


@router.post("/", response_model=CreateProductResponseSchema)
async def create_product(request_body: CreateProductRequestSchema):
    """
    Method to create a product.

    Args:
        request_body (CreateProductRequestSchema): A CreateProductRequestSchema object.

    Returns:
        Product: A Product object.
    """
    product_app_services = ProductAppServices()
    return await product_app_services.create_product(data=request_body)


@router.patch("/{product_id}", response_model=UpdateProductResponseSchema)
async def update_product(product_id: str, request_body: UpdateProductRequestSchema):
    """
    Method to update a product by id.

    Args:
        product_id (str): Product id.
        request_body (UpdateProductRequestSchema): A UpdateProductRequestSchema object.

    Returns:
        Product: A Product object.
    """
    product_app_services = ProductAppServices()
    return await product_app_services.update_product_by_id(
        product_id=product_id,
        data=request_body,
    )


@router.delete("/{product_id}", response_model=DeleteProductResponseSchema)
async def delete_product(product_id: str):
    """
    Method to delete a product by id.

    Args:
        product_id (str): Product id.

    Returns:
        Product: A Product object.
    """
    product_app_services = ProductAppServices()
    return await product_app_services.delete_product_by_id(product_id=product_id)
