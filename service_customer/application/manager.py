import logging

from django.db import IntegrityError

from service_customer.application.dto import CustomerDto
from service_customer.application.storage import CustomerStorage
from service_customer.domain import exceptions as ex
from service_customer.domain.enums import ErrorCodes, SuccessCodes
from service_product.application.dto import ProductDto

# TODO criar um mecanismo de log centralizado
log = logging.getLogger(__name__)


class CustomerManager:

    def __init__(self, storage: CustomerStorage) -> None:
        self.storage: CustomerStorage = storage

    def list_reserved_products(self, customer_id: int) -> list[ProductDto]:
        """List reserved products by customer"""
        return self.storage.list_reserved_products(customer_id)

    def create_new_customer(self, customer_dto: CustomerDto):
        customer = customer_dto.to_domain()
        try:
            if customer.is_valid():
                self.storage.save_customer(customer_dto)
        except ex.CustomerEmailCannotBeNoneOrBlankException:
            return {
                "message": ErrorCodes.CUSTOMER_EMAIL_CANNOT_BE_NONE_OR_BLANK.value,
                "code": ErrorCodes.CUSTOMER_EMAIL_CANNOT_BE_NONE_OR_BLANK.name,
            }
        except ex.CustomerDocumentInvalidLength:
            return {
                "message": ErrorCodes.CUSTOMER_DOCUMENT_HAS_INVALID_LEN.value,
                "code": ErrorCodes.CUSTOMER_DOCUMENT_HAS_INVALID_LEN.name,
            }
        except ex.CustomerNameCannotBeNoneOrBlankException:
            return {
                "message": ErrorCodes.CUSTOMER_NAME_CANNOT_BE_NONE_OR_BLANK.value,
                "code": ErrorCodes.CUSTOMER_NAME_CANNOT_BE_NONE_OR_BLANK.name,
            }
        except ex.CustomerNameTooShortException:
            return {
                "message": ErrorCodes.CUSTOMER_NAME_TOO_SHORT.value,
                "code": ErrorCodes.CUSTOMER_NAME_TOO_SHORT.name,
            }
        except IntegrityError:
            return {
                "message": ErrorCodes.CUSTOMER_ALREADY_EXISTS.value,
                "code": ErrorCodes.CUSTOMER_ALREADY_EXISTS.name,
            }
        except Exception as e:
            log.exception(e, exc_info=True)
            return {
                "message": ErrorCodes.CUSTOMER_UNDEFINED_ERROR.value,
                "code": ErrorCodes.CUSTOMER_UNDEFINED_ERROR.name,
            }

        return {
            "message": SuccessCodes.SUCCESS.value,
            "code": SuccessCodes.SUCCESS.name,
        }
