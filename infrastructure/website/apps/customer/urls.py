from django.urls import path

from .views import CreateNewCustomer, ListReservedProductsView

app_name = "customer"
urlpatterns = [
    path("", CreateNewCustomer.as_view(), name="create-new-customer"),
    path(
        "customer/<int:id_customer>/reservations",
        ListReservedProductsView.as_view(),
        name="product-list-all",
    ),
]
