from django.shortcuts import render
from django.views.generic.base import View

from infrastructure.website.apps.customer.repositories import CustomerRepository
from service_customer.application.dto import CustomerDto
from service_customer.application.manager import CustomerManager
from service_customer.domain.enums import SuccessCodes


class CreateNewCustomer(View):
    def get(self, request, *args, **kwargs):
        dto = CustomerDto("Marcus", "marcus@sistema.com", "11111111111")
        repository = CustomerRepository()
        manager = CustomerManager(repository)
        response = manager.create_new_customer(dto)

        if response["code"] == SuccessCodes.SUCCESS:
            return render(
                request,
                "customer/index.html",
                {"response": "Customer Cadastrado com sucesso"},
            )

        return render(request, "customer/index.html", {"response": response})

    def post(self, request, *args, **kwargs):
        raise NotImplementedError()


class ListReservedProductsView(View):
    def get(self, request, *args, **kwargs):
        id_customer: int = kwargs["id_customer"]
        repository = CustomerRepository()
        manager = CustomerManager(repository)
        products = manager.list_reserved_products(id_customer)
        return render(request, "product/index.html", {"response": products})
