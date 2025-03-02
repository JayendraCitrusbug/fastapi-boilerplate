import uuid

from src.domain.products.services import ProductDomainServices
from src.infrastructure.response_handler import ResponseHandler


class ProductAppServices:
    def __init__(self):
        self.product_domain_services = ProductDomainServices()

    async def get_products_list(self):
        try:
            data = self.product_domain_services.get_products_list()
            return ResponseHandler.success(
                message="Products retrieved successfully",
                data=data,
            )
        except Exception as e:
            return ResponseHandler.error(exception=e)

    async def get_products_by_uset_id(self, user_id: uuid.UUID):
        try:
            return self.product_domain_services.get_products_by_user_id(user_id=user_id)
        except Exception as e:
            return ResponseHandler.error(exception=e)

    async def get_product_details_by_id(self, product_id: uuid.UUID):
        try:
            return self.product_domain_services.get_product_by_id(product_id=product_id)
        except Exception as e:
            return ResponseHandler.error(exception=e)

    async def create_product(self, data):
        try:
            return self.product_domain_services.create_product(data=data)
        except Exception as e:
            return ResponseHandler.error(exception=e)

    async def update_product_by_id(self, product_id: uuid.UUID, data):
        try:
            return self.product_domain_services.update_product_by_id(
                product_id=product_id,
                data=data,
            )
        except Exception as e:
            return ResponseHandler.error(exception=e)

    async def delete_product_by_id(self, product_id: uuid.UUID):
        try:
            return self.product_domain_services.delete_product_by_id(
                product_id=product_id
            )
        except Exception as e:
            return ResponseHandler.error(exception=e)
