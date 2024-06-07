from django.db import models
from common.models import CommonModel


# Create your models here.
class Camera(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(
        "brands.brand",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    megapixels = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    iso = models.CharField(max_length=50, null=True, blank=True)
    image_stabilization = models.BooleanField(default=False)
    price_won = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True
    )
    price_dollar = models.DecimalField(
        max_digits=20, decimal_places=2, null=True, blank=True
    )
    release_date = models.DateField(null=True, blank=True)
