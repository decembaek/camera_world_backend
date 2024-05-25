from django.db import models
from common.models import CommonModel


# Create your models here.
class Review(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    payload = models.TextField()
    rating = models.PositiveIntegerField()
    gallery = models.ForeignKey(
        "galleries.gallery",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    camera = models.ForeignKey(
        "cameras.camera",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
