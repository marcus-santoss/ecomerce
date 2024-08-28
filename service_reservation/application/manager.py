import logging

from django.db import IntegrityError

from service_customer.application.dto import CustomerDto
from service_product.application.dto import ProductDto
from service_reservation.application.dto import ReservationDto
from service_reservation.application.storage import ReservationStorage
from service_reservation.domain import exceptions as ex
from service_reservation.domain.enums import ErrorCodes, SuccessCodes

# TODO criar um mecanismo de log centralizado
log = logging.getLogger(__name__)


class ReservationManager:

    def __init__(self, storage: ReservationStorage) -> None:
        self.storage: ReservationStorage = storage

    def get_random_user(self) -> CustomerDto:
        return self.storage.get_random_customer()

    def get_product_by_id(self, product_id: int) -> ProductDto:
        return self.storage.get_product_by_id(product_id)

    def create_new_reservation(self, reservation_dto: ReservationDto):
        reservation = reservation_dto.to_domain()
        try:
            if reservation.is_valid():
                self.storage.save_reservation(reservation_dto)
        except ex.ReservationProductUnavailableException:
            return {
                "message": ErrorCodes.RESERVATION_PRODUCT_UNAVAILABLE.value,
                "code": ErrorCodes.RESERVATION_PRODUCT_UNAVAILABLE.name,
            }
        except IntegrityError as e:
            log.exception(e, exc_info=True)
            return {
                "message": ErrorCodes.RESERVATION_ALREADY_EXISTS.value,
                "code": ErrorCodes.RESERVATION_ALREADY_EXISTS.name,
            }
        except Exception as e:
            log.exception(e, exc_info=True)
            if "Customer matching" in str(e):
                return {
                    "message": ErrorCodes.RESERVATION_CUSTOMER_NOT_FOUND.value,
                    "code": ErrorCodes.RESERVATION_CUSTOMER_NOT_FOUND.name,
                }

            if "Product matching" in str(e):
                return {
                    "message": ErrorCodes.RESERVATION_PRODUCT_NOT_FOUND.value,
                    "code": ErrorCodes.RESERVATION_PRODUCT_NOT_FOUND.name,
                }
            return {
                "message": ErrorCodes.RESERVATION_UNDEFINED_ERROR.value,
                "code": ErrorCodes.RESERVATION_UNDEFINED_ERROR.name,
            }

        return {
            "message": SuccessCodes.PRODUCT_RESERVED_WITH_SUCCESS.value,
            "code": SuccessCodes.PRODUCT_RESERVED_WITH_SUCCESS.name,
        }
