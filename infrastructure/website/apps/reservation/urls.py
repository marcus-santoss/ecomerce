from django.urls import path

from infrastructure.website.apps.reservation.views import CreateNewReservation

app_name = "reservation"
urlpatterns = [
    path(
        "products/<int:product_id>/reserve/",
        CreateNewReservation.as_view(),
        name="new-reservation",
    )
]
