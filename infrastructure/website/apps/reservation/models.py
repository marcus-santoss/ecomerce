from apps.customer.models import Customer
from apps.product.models import Product
from django.db import models


class Reservation(models.Model):
    customer = models.ForeignKey(
        Customer, related_name="products_reserveds", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="reservations", on_delete=models.CASCADE
    )
    reservation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.product.name} Reserved until {self.reservation_date:%Y-%m-%d}"

    class Meta:
        unique_together = (("customer", "product", "reservation_date"),)
