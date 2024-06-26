from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    gallery = models.ManyToManyField(
        "galleries.gallery",
        related_name="tags",
    )
