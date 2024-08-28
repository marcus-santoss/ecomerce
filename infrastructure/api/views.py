from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from infrastructure.website.apps.customer.repositories import CustomerRepository
from infrastructure.website.apps.product.repositories import ProductRepository
from infrastructure.website.apps.reservation.repositories import ReservationRepository
from service_customer.application.manager import CustomerManager
from service_product.application.manager import ProductManager
from service_reservation.application.dto import ReservationDto
from service_reservation.application.manager import ReservationManager
from service_reservation.domain.enums import SuccessCodes


class ListAllProductsViewSet(ViewSet):
    def list(self, request: Request) -> Response:
        repository = ProductRepository()
        manager = ProductManager(repository)
        products = manager.list_all_products()
        # Parse data to dict
        data = [p.to_dict() for p in products]

        return Response(data=data, status=status.HTTP_200_OK)


class ListReservedProductsViewSet(ViewSet):
    def get(self, request: Request, *args, **kwargs) -> Response:
        repository = CustomerRepository()
        manager = CustomerManager(repository)
        products = manager.list_reserved_products(**kwargs)
        data = [d.to_dict() for d in products]
        return Response(data=data, status=status.HTTP_200_OK)


class MakeReservationViewSet(ViewSet):
    def create(self, request: Request, *args, **kwargs) -> Response:
        repository = ReservationRepository()
        manager = ReservationManager(repository)

        dto = ReservationDto(
            customer_dto=manager.get_random_user(),
            product_dto=manager.get_product_by_id(**kwargs),
        )
        response = manager.create_new_reservation(dto)

        if response["code"] == SuccessCodes.PRODUCT_RESERVED_WITH_SUCCESS:
            return Response(data=response, status=status.HTTP_200_OK)

        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
