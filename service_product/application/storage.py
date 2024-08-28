import abc

from service_product.application.dto import ProductDto


class ProductStorage(abc.ABC):

    @abc.abstractmethod
    def save_product(self, product_dto: ProductDto):
        pass

    @abc.abstractmethod
    def list_all_products(self):
        pass
