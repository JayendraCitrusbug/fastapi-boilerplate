import uuid

from sqlalchemy import Column, Float, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID

from src.domain.utils import ActivityTracking


class Product(ActivityTracking):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
