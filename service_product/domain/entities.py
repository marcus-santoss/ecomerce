from dataclasses import dataclass

from service_product.domain.enums import ProductStatusCodes
from service_product.domain.exceptions import (
    ProductNameCannotBeBlankOrNoneException,
    ProductWithInvalidPriceException,
    ProductWithInvalidStatusOnSavingException,
)


@dataclass
class Product:
    name: str
    description: str
    price: float
    status: ProductStatusCodes = None
    id: int = None

    def __post_init__(self):
        if self.status is None:
            self.status = ProductStatusCodes.PRODUCT_AVAILABLE

    def is_valid(self):
        if self.name is None:
            raise ProductNameCannotBeBlankOrNoneException(
                "The Product name is required"
            )

        if self.price <= 0:
            raise ProductWithInvalidPriceException("The Product price is invalid")

        if self.status != ProductStatusCodes.PRODUCT_AVAILABLE:
            raise ProductWithInvalidStatusOnSavingException(
                "Product with invalid status for saving state"
            )

        return True
