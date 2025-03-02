from typing import Optional

from pydantic import BaseModel


class CreateProductRequestSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


class UpdateProductRequestSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
