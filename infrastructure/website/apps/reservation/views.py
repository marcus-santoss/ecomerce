from apps.reservation.repositories import ReservationRepository
from django.shortcuts import render
from django.views.generic.base import View

from service_reservation.application.dto import ReservationDto
from service_reservation.application.manager import ReservationManager
from service_reservation.domain.enums import SuccessCodes


class CreateNewReservation(View):
    def get(self, request, *args, **kwargs):
        product_id: int = kwargs.get("product_id")
        repository = ReservationRepository()
        manager = ReservationManager(repository)

        dto = ReservationDto(
            customer_dto=manager.get_random_user(),
            product_dto=manager.get_product_by_id(product_id),
        )
        response = manager.create_new_reservation(dto)

        if response["code"] == SuccessCodes.PRODUCT_RESERVED_WITH_SUCCESS:
            return render(
                request,
                "reservation/index.html",
                {"response": "Reserva criada com sucesso"},
            )

        return render(request, "reservation/index.html", {"response": response})

    def post(self, request, *args, **kwargs):
        raise NotImplementedError()
