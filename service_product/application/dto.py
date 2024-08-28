from dataclasses import dataclass

from service_product.domain.entities import Product
from service_product.domain.enums import ProductStatusCodes


@dataclass
class ProductDto:
    name: str
    description: str
    price: float
    status: ProductStatusCodes = None
    id: int = None

    def __post_init__(self):
        if self.status is None:
            self.status = ProductStatusCodes.PRODUCT_AVAILABLE

    def __iter__(self):
        if self.id is not None:
            yield "id", self.id
        yield "name", self.name
        yield "description", self.description
        yield "price", self.price
        yield "status", self.status

    def to_domain(self) -> Product:
        return Product(
            name=self.name,
            description=self.description,
            price=self.price,
            status=self.status,
        )

    def to_dict(self) -> dict:
        return dict(self)
