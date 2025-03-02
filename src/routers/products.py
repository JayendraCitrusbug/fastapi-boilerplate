from fastapi import APIRouter

from src.application.products import ProductAppServices
from src.schema.products import CreateProductRequestSchema, UpdateProductRequestSchema

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("/")
async def get_all_products():
    product_app_services = ProductAppServices()
    return await product_app_services.get_products_list()


@router.get("/{product_id}")
async def get_product_by_id(product_id: str):
    product_app_services = ProductAppServices()
    return await product_app_services.get_product_details_by_id(product_id=product_id)


@router.post("/")
async def create_product(request_body: CreateProductRequestSchema):
    product_app_services = ProductAppServices()
    return await product_app_services.create_product(data=request_body)


@router.patch("/{product_id}")
async def update_product(product_id: str, request_body: UpdateProductRequestSchema):
    product_app_services = ProductAppServices()
    return await product_app_services.update_product_by_id(
        product_id=product_id,
        data=request_body,
    )


@router.delete("/{product_id}")
async def delete_product(product_id: str):
    product_app_services = ProductAppServices()
    return await product_app_services.delete_product_by_id(product_id=product_id)
