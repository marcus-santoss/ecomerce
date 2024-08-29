from django.db import models

PRODUCT_STATUS_CHOICES = (
    ("PRODUCT_AVAILABLE", "AVAILABLE"),
    ("PRODUCT_RESERVED", "RESERVED"),
    ("PRODUCT_UNAVAILABLE", "UNAVAILABLE"),
)


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.CharField(
        max_length=30, choices=PRODUCT_STATUS_CHOICES, default="PRODUCT_AVAILABLE"
    )

    def __str__(self) -> str:
        return self.name
