from django.urls import path

from infrastructure.api.views import (
    ListAllProductsViewSet,
    ListReservedProductsViewSet,
    MakeReservationViewSet,
)

app_name = "api"

urlpatterns = [
    path("products/", ListAllProductsViewSet.as_view({"get": "list"}), name="products"),
    path(
        "customer/<int:customer_id>/reservations/",
        ListReservedProductsViewSet.as_view({"get": "get"}),
        name="list-reserved-products",
    ),
    path(
        "products/<int:product_id>/reserve/",
        MakeReservationViewSet.as_view({"post": "create"}),
        name="make-reservation",
    ),
]
