from dataclasses import dataclass
from datetime import datetime, timedelta

from service_customer.domain.entities import Customer
from service_product.domain.entities import Product
from service_reservation.domain.exceptions import (
    ReservationProductNotFoundException,
    ReservationProductUnavailableException,
)


@dataclass
class Reservation:
    customer: Customer
    product: Product
    reservation_date: datetime.date = datetime.now().date()
    id: int = None

    @property
    def expiration_date(self) -> datetime.date:
        return self.reservation_date + timedelta(days=3)

    @property
    def is_expired(self) -> bool:
        return self.expiration_date < datetime.now().date()

    def is_valid(self) -> bool:
        self.customer.is_valid()
        self.product.is_valid()

        if self.is_expired:
            raise ReservationProductUnavailableException("Product Unavailable")

        if self.customer is None:
            raise ReservationProductNotFoundException("Product not found")

        if self.product is None:
            raise ReservationProductNotFoundException("Product not found")

        return True
