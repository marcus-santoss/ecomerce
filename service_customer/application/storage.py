import abc

from service_customer.application.dto import CustomerDto
from service_product.application.dto import ProductDto


class CustomerStorage(abc.ABC):

    @abc.abstractmethod
    def save_customer(self, customer_dto: CustomerDto):
        pass

    @abc.abstractmethod
    def list_reserved_products(self, id_customer: int) -> list[ProductDto]:
        pass
