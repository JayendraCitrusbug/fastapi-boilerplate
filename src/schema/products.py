from typing import Optional
from uuid import UUID

from fastapi import status
from pydantic import BaseModel, ConfigDict


class ProductResponseModel(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    price: float
    quantity: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426655440000",
                "name": "Product 1",
                "description": "This is a product",
                "price": 10.99,
                "quantity": 5,
            }
        }
    )


class CreateProductRequestSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Product 1",
                "description": "This is a new product",
                "price": 10.99,
                "quantity": 5,
            }
        }
    )


class UpdateProductRequestSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Product 1",
                "description": "This is an updated product",
                "price": 14.99,
                "quantity": 10,
            }
        }
    )


class GetProductsListingsResponseSchema(BaseModel):
    success: bool = True
    status_code: int = status.HTTP_200_OK
    message: str = "Products retrieved successfully"
    data: list[ProductResponseModel]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "status_code": 200,
                "message": "Products retrieved successfully",
                "data": [
                    {
                        "id": "123e4567-e89b-12d3-a456-426655440000",
                        "name": "Product 1",
                        "description": "This is a product",
                        "price": 10.99,
                        "quantity": 5,
                    },
                    {
                        "id": "123e4567-e89b-12d3-a456-426655440001",
                        "name": "Product 2",
                        "description": "This is another product",
                        "price": 19.99,
                        "quantity": 3,
                    },
                ],
            }
        }
    )


class GetProductResponseSchema(BaseModel):
    success: bool = True
    status_code: int = status.HTTP_200_OK
    message: str = "Product retrieved successfully"
    data: ProductResponseModel

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "status_code": 200,
                "message": "Product retrieved successfully",
                "data": {
                    "id": "123e4567-e89b-12d3-a456-426655440000",
                    "name": "Product 1",
                    "description": "This is a product",
                    "price": 10.99,
                    "quantity": 5,
                },
            }
        }
    )


class CreateProductResponseSchema(BaseModel):
    success: bool = True
    status_code: int = status.HTTP_201_CREATED
    message: str = "Product created successfully"
    data: ProductResponseModel

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "status_code": 201,
                "message": "Product created successfully",
                "data": {
                    "id": "123e4567-e89b-12d3-a456-426655440000",
                    "name": "Product 1",
                    "description": "This is a product",
                    "price": 10.99,
                    "quantity": 5,
                },
            }
        }
    )


class UpdateProductResponseSchema(BaseModel):
    success: bool = True
    status_code: int = status.HTTP_200_OK
    message: str = "Product updated successfully"
    data: ProductResponseModel

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "status_code": 200,
                "message": "Product updated successfully",
                "data": {
                    "id": "123e4567-e89b-12d3-a456-426655440000",
                    "name": "Product 1",
                    "description": "This is an updated product",
                    "price": 14.99,
                    "quantity": 10,
                },
            }
        }
    )


class DeleteProductResponseSchema(BaseModel):
    success: bool = True
    status_code: int = status.HTTP_200_OK
    message: str = "Product deleted successfully"
    data: ProductResponseModel

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "status_code": 200,
                "message": "Product deleted successfully",
                "data": "123e4567-e89b-12d3-a456-426655440000",
            }
        }
    )
