from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    document = models.CharField(max_length=11, unique=True, null=False, blank=False)

    def __str__(self) -> str:
        return self.name
