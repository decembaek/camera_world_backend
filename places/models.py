from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    country = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
