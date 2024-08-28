from apps.customer.models import Customer as CustomerModel
from apps.product.models import Product as ProductModel
from apps.reservation.models import Reservation as ReservationModel
from django.db.transaction import atomic

from service_customer.application.dto import CustomerDto
from service_product.application.dto import ProductDto
from service_product.domain.enums import ProductStatusCodes
from service_reservation.application.dto import ReservationDto
from service_reservation.application.storage import ReservationStorage


# ReservationStorage: Contrato de dados com a camada superior
class ReservationRepository(ReservationStorage):

    def get_product_by_id(self, product_id: int) -> ProductDto:
        product = ProductModel.objects.get(id=product_id)
        return ProductDto(
            id=product_id,
            name=product.name,
            price=product.price,
            description=product.description,
        )

    def get_random_customer(self) -> CustomerDto:
        customer = CustomerModel.objects.order_by("?").first()
        return CustomerDto(
            id=customer.id,
            name=customer.name,
            email=customer.email,
            document=customer.document,
        )

    @atomic
    def save_reservation(self, reservation_dto: ReservationDto):
        # Saves reservation
        reservation = self._reservation_dto_to_model(reservation_dto)
        reservation.save()

        # Update product status
        reservation.product.status = ProductStatusCodes.PRODUCT_RESERVED.value
        reservation.product.save()

    @staticmethod
    def _reservation_dto_to_model(reservation_dto: ReservationDto) -> ReservationModel:
        customer = CustomerModel.objects.get(pk=reservation_dto.customer_dto.id)
        product = ProductModel.objects.get(pk=reservation_dto.product_dto.id)

        return ReservationModel(
            customer_id=customer.id,
            product_id=product.id,
            reservation_date=reservation_dto.reservation_date,
        )
