from apps.customer.models import Customer
from apps.reservation.models import Reservation

from service_customer.application.dto import CustomerDto
from service_customer.application.storage import CustomerStorage
from service_product.application.dto import ProductDto


# CustomerStorage: Contrato de dados com a camada superior
class CustomerRepository(CustomerStorage):

    @staticmethod
    def _customer_dto_to_model(customer_dto: CustomerDto) -> Customer:
        return Customer(**customer_dto.to_dict())

    @staticmethod
    def _reservation_model_to_product_dto(reservation_model: Reservation) -> ProductDto:
        return ProductDto(
            id=reservation_model.product.id,
            name=reservation_model.product.name,
            description=reservation_model.product.description,
            price=reservation_model.product.price,
            status=reservation_model.product.status,
        )

    def list_reserved_products(self, id_customer: int) -> list[ProductDto]:
        """List all reserved products."""
        products_dto: list[ProductDto] = []
        products = Reservation.objects.filter(customer_id=id_customer)
        if not products.exists():
            return products_dto

        for product in products:
            products_dto.append(self._reservation_model_to_product_dto(product))

        return products_dto

    def save_customer(self, customer_dto: CustomerDto):
        customer = self._customer_dto_to_model(customer_dto)
        customer.save()
