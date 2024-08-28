import abc

from service_customer.application.dto import CustomerDto
from service_product.application.dto import ProductDto
from service_reservation.application.dto import ReservationDto


class ReservationStorage(abc.ABC):

    @abc.abstractmethod
    def save_reservation(self, reservation_dto: ReservationDto):
        pass

    @abc.abstractmethod
    def get_random_customer(self) -> CustomerDto:
        pass

    @abc.abstractmethod
    def get_product_by_id(self, product_id: int) -> ProductDto:
        pass
