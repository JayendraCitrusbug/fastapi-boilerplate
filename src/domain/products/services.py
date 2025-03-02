import uuid
from dataclasses import asdict, dataclass
from typing import Optional

from config.db_connection import db_service
from src.domain.products.models import Product
from src.infrastructure.response_handler import ResponseHandler


@dataclass(frozen=True)
class ProductDataClass:
    """
    Data class for Product model.
    """

    name: str
    description: Optional[str]
    price: float
    quantity: int


class ProductFactory:
    """
    ProductFactory class for Product model for creating runtime Product Objects
    """

    @staticmethod
    def build_entity_with_id(data: ProductDataClass) -> Product:
        """
        Method to create runtime Product object using dataclass.

        Args:
            data (Dict): A dictionary containing broker information.
                - name (str): Name of the broker.
                - description (str): Description of the broker.
                - price (float): Price of the broker.
                - quantity (int): Quantity of the broker.

        Returns:
            Product: A runtime Product object.
        """
        return Product(id=uuid.uuid4(), **asdict(data))


class ProductDomainServices:
    def __init__(self):
        self.db_session = db_service.get_session()

    @staticmethod
    def get_product_factory():
        try:
            return ProductFactory
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def __get_product_repo(self):
        try:
            return self.db_session.query(Product)
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def get_products_list(self):
        try:
            return self.__get_product_repo().all()
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def get_products_by_user_id(self, user_id: uuid.UUID):
        try:
            return self.__get_product_repo().filter_by(user_id=user_id).all()
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def get_product_by_id(self, product_id: uuid.UUID):
        try:
            return self.__get_product_repo().get(product_id)
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def create_product(self, data: ProductDataClass):
        try:
            product = self.get_product_factory().build_entity_with_id(data)
            self.db_session.add(product)
            self.db_session.commit()
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def update_product_by_id(self, product_id: uuid.UUID, data: ProductDataClass):
        try:
            product = self.get_product_by_id(product_id)
            return product
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def delete_product_by_id(self, product_id: uuid.UUID):
        try:
            product = self.__get_product_repo().delete(product_id)
            return product
        except Exception as e:
            return ResponseHandler.error(exception=e)
