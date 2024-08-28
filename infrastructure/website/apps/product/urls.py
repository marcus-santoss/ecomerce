from django.urls import path

from infrastructure.website.apps.product.views import (
    CreateNewProduct,
    ListProductsView,
)

app_name = "product"
urlpatterns = [
    path("product/new/", CreateNewProduct.as_view(), name="product-new"),
    path("products/", ListProductsView.as_view(), name="product-list-all"),
]
