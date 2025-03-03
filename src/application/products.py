import uuid

from fastapi import status

from src.domain.products.services import ProductDataClass, ProductDomainServices
from src.infrastructure.exception_handler import BaseHTTPException
from src.infrastructure.response_handler import ResponseHandler
from src.schema.products import CreateProductRequestSchema, UpdateProductRequestSchema


class ProductAppServices:
    def __init__(self):
        """
        Constructor for ProductAppServices class.
        """
        self.product_domain_services = ProductDomainServices()

    async def get_products_list(self):
        """
        Method to get all products.

        Returns:
            List[Product]: A list of all products.
        """

        try:
            data = self.product_domain_services.get_products_list()
            return ResponseHandler.success(
                message="Products retrieved successfully",
                data=data,
            )
        except Exception as e:
            return ResponseHandler.error(exception=e)

    async def get_products_by_user_id(self, user_id: uuid.UUID):
        """
        Method to get all products by user id.

        Args:
            user_id (uuid.UUID): User id.

        Returns:
            List[Product]: A list of all products.
        """

        try:
            products = self.product_domain_services.get_products_by_user_id(
                user_id=user_id
            )
            return ResponseHandler.success(
                message="Products retrieved successfully",
                data=products,
            )
        except Exception as e:
            return ResponseHandler.error(exception=e)

    async def get_product_details_by_id(
        self, product_id: uuid.UUID, raise_exception: bool = False
    ):
        """
        Method to get a product by id.

        Args:
            product_id (uuid.UUID): Product id.

        Returns:
            Product: A Product object.
        """

        try:
            if raise_exception:
                raise BaseHTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    message="Product with provided ID not found",
                )

            product = self.product_domain_services.get_product_by_id(
                product_id=product_id
            )
            return ResponseHandler.success(
                message="Product retrieved successfully",
                data=product,
            )
        except Exception as e:
            return ResponseHandler.error(exception=e)

    async def create_product(self, data: CreateProductRequestSchema):
        """
        Method to create a product.

        Args:
            data (CreateProductRequestSchema): A CreateProductRequestSchema object.

        Returns:
            Product: A Product object.
        """

        try:
            discounted_price = data.price * 0.75
            product_dataclass = ProductDataClass(
                name=data.name,
                description=data.description,
                price=discounted_price,
                quantity=data.quantity,
            )
            product = (
                self.product_domain_services.get_product_factory().build_entity_with_id(
                    data=product_dataclass
                )
            )
            product = self.product_domain_services.create_product(product=product)
            return ResponseHandler.success(
                message="Product created successfully",
                data=product,
            )
        except Exception as e:
            return ResponseHandler.error(exception=e)

    async def update_product_by_id(
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
            product = self.product_domain_services.update_product_by_id(
                product_id=product_id,
                data=data,
            )
            return ResponseHandler.success(
                message="Product updated successfully",
                data=product,
            )
        except Exception as e:
            return ResponseHandler.error(exception=e)

    async def delete_product_by_id(self, product_id: uuid.UUID):
        """
        Method to delete a product by id.

        Args:
            product_id (uuid.UUID): Product id.

        Returns:
            Product: A Product object.
        """

        try:
            product = self.product_domain_services.delete_product_by_id(
                product_id=product_id
            )
            return ResponseHandler.success(
                message="Product deleted successfully",
                data=product.id,
            )
        except Exception as e:
            return ResponseHandler.error(exception=e)
