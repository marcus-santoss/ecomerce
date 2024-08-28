from apps.product.repositories import ProductRepository
from django.shortcuts import render
from django.views.generic.base import View

from service_customer.domain.enums import SuccessCodes
from service_product.application.dto import ProductDto
from service_product.application.manager import ProductManager


class ListProductsView(View):
    def get(self, request, *args, **kwargs):
        repository = ProductRepository()
        manager = ProductManager(repository)
        products = manager.list_all_products()
        return render(request, "product/index.html", {"response": products})


class CreateNewProduct(View):
    def get(self, request, *args, **kwargs):
        dto = ProductDto(
            name="Camiseta Feminina",
            description="Camiseta preta feminina tamanho P",
            price=49.9,
        )
        repository = ProductRepository()
        manager = ProductManager(repository)
        response = manager.create_new_product(dto)

        if response["code"] == SuccessCodes.SUCCESS:
            return render(
                request,
                "product/index.html",
                {"response": "Customer Cadastrado com sucesso"},
            )

        return render(request, "product/index.html", {"response": response})

    def post(self, request, *args, **kwargs):
        raise NotImplementedError()
