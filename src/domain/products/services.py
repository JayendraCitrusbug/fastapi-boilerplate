import uuid
from dataclasses import asdict, dataclass
from typing import Optional

from sqlalchemy import update

from config.db_connection import db_service
from src.domain.products.models import Product
from src.infrastructure.response_handler import ResponseHandler
from src.schema.products import UpdateProductRequestSchema


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
        """
        Constructor for ProductDomainServices class.
        """
        self.db_session = db_service.get_session()

    @staticmethod
    def get_product_factory():
        """
        Method to get ProductFactory object.

        Returns:
            ProductFactory: A ProductFactory object.
        """

        try:
            return ProductFactory
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def __get_product_repo(self):
        """
        Method to get Product repository.

        Returns:
            Product: A Product repository.
        """

        try:
            return self.db_session.query(Product)
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def get_products_list(self):
        """
        Method to get all products.

        Returns:
            List[Product]: A list of all products.
        """

        try:
            return self.__get_product_repo().all()
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def get_products_by_user_id(self, user_id: uuid.UUID):
        """
        Method to get all products by user id.

        Args:
            user_id (uuid.UUID): User id.

        Returns:
            List[Product]: A list of all products.
        """

        try:
            return self.__get_product_repo().filter_by(user_id=user_id).all()
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def get_product_by_id(self, product_id: uuid.UUID):
        """
        Method to get a product by id.

        Args:
            product_id (uuid.UUID): Product id.

        Returns:
            Product: A Product object.
        """

        try:
            product = self.__get_product_repo().get(product_id)
            return product
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def create_product(self, product: Product):
        """
        Method to create a product.

        Args:
            product (Product): A Product object.

        Returns:
            Product: A Product object.
        """

        try:
            self.db_session.add(product)
            self.db_session.commit()
            self.db_session.refresh(product)
            return product
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def update_product_by_id(
        self, product_id: uuid.UUID, data: UpdateProductRequestSchema
    ):
        """
        Method to update a product by id.

        Args:
            product_id (uuid.UUID): Product id.
            data (UpdateProductRequestSchema): A UpdateProductRequestSchema object.

        Returns:
            Product: A Product object.
        """

        try:
            product = (
                update(Product)
                .where(Product.id == product_id)
                .values(
                    **data.model_dump(exclude_unset=True),
                )
            )
            self.db_session.execute(product)
            self.db_session.commit()
            return product
        except Exception as e:
            return ResponseHandler.error(exception=e)

    def delete_product_by_id(self, product_id: uuid.UUID):
        """
        Method to delete a product by id.

        Args:
            product_id (uuid.UUID): Product id.

        Returns:
            Product: A Product object.
        """

        try:
            product = self.__get_product_repo().delete(product_id)
            return product
        except Exception as e:
            return ResponseHandler.error(exception=e)
