from dataclasses import dataclass
from datetime import datetime

from service_customer.application.dto import CustomerDto
from service_product.application.dto import ProductDto
from service_reservation.domain.entities import Reservation


@dataclass
class ReservationDto:
    customer_dto: CustomerDto
    product_dto: ProductDto
    reservation_date: datetime.date = datetime.now().date()
    id: int = None

    def __iter__(self):
        yield "id", self.id
        yield "customer", self.customer_dto
        yield "product", self.product_dto
        yield "reservation_date", self.reservation_date

    def to_dict(self):
        return dict(self)

    def to_domain(self):
        return Reservation(
            customer=self.customer_dto.to_domain(),
            product=self.product_dto.to_domain(),
            reservation_date=self.reservation_date,
        )
