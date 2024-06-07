from django.db import models


# Create your models here.
class Place(models.Model):
    gallery = models.ForeignKey(
        "galleries.gallery",
        on_delete=models.CASCADE,
        related_name="places",
        null=True,
        blank=True,
    )
    photo = models.ForeignKey(
        "medias.photo",
        on_delete=models.CASCADE,
        related_name="photos",
        null=True,
        blank=True,
    )
    video = models.ForeignKey(
        "medias.video",
        on_delete=models.CASCADE,
        related_name="videos",
        null=True,
        blank=True,
    )
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
