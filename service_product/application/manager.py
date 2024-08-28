import logging

from django.db import IntegrityError

from service_customer.domain.enums import SuccessCodes
from service_product.application.dto import ProductDto
from service_product.application.storage import ProductStorage
from service_product.domain.enums import ErrorCodes
from service_product.domain.exceptions import (
    ProductNameCannotBeBlankOrNoneException,
    ProductWithInvalidPriceException,
    ProductWithInvalidStatusOnSavingException,
)

# TODO criar um mecanismo de log centralizado
log = logging.getLogger(__name__)


class ProductManager:
    """Product Service Layer"""

    def __init__(self, storage: ProductStorage) -> None:
        self.storage: ProductStorage = storage

    def list_all_products(self) -> list[ProductDto]:
        """List all products in database"""
        return self.storage.list_all_products()

    def create_new_product(self, product_dto: ProductDto):
        """Save a new product in database"""
        product = product_dto.to_domain()

        try:
            if product.is_valid():
                self.storage.save_product(product_dto)
        except ProductNameCannotBeBlankOrNoneException:
            return {
                "message": ErrorCodes.PRODUCT_NAME_CANNOT_BE_BLANK_OR_NONE.value,
                "code": ErrorCodes.PRODUCT_NAME_CANNOT_BE_BLANK_OR_NONE.name,
            }
        except ProductWithInvalidPriceException:
            return {
                "message": ErrorCodes.PRODUCT_WITH_INVALID_PRICE.value,
                "code": ErrorCodes.PRODUCT_WITH_INVALID_PRICE.name,
            }
        except ProductWithInvalidStatusOnSavingException:
            return {
                "message": ErrorCodes.PRODUCT_WITH_INVALID_STATUS_FOR_SAVE.value,
                "code": ErrorCodes.PRODUCT_WITH_INVALID_STATUS_FOR_SAVE.name,
            }
        except IntegrityError:
            return {
                "message": ErrorCodes.PRODUCT_ALREADY_EXISTS.value,
                "code": ErrorCodes.PRODUCT_ALREADY_EXISTS.name,
            }
        except Exception as e:
            log.exception(e, exc_info=True)
            return {
                "message": ErrorCodes.PRODUCT_UNDEFINED_ERROR.value,
                "code": ErrorCodes.PRODUCT_UNDEFINED_ERROR.name,
            }

        return {
            "message": SuccessCodes.SUCCESS.value,
            "code": SuccessCodes.SUCCESS.name,
        }
