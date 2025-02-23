from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("/")
async def get_all_products():
    return [{"name": "Product 1"}, {"name": "Product 2"}]
