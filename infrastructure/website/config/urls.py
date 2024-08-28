import sys

from django.contrib import admin
from django.urls import include, path

sys.path.append("infrastructure")

urlpatterns = [
    path("", include("apps.customer.urls", namespace="customer")),
    path("", include("apps.product.urls", namespace="product")),
    path("", include("apps.reservation.urls", namespace="reservation")),
    path("api/", include("api.urls", namespace="api")),
    path("admin/", admin.site.urls),
]
