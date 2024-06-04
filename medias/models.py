from django.db import models
from common.models import CommonModel


# Create your models here.
class Photo(CommonModel):
    file = models.URLField()
    description = models.CharField(max_length=300)
    gallery = models.ForeignKey(
        "galleries.gallery",
        on_delete=models.SET_NULL,
        null=True,
        related_name="photos",
    )

    def __str__(self):
        return f"gallery_{self.gallery}"


class Video(CommonModel):
    file = models.URLField()
    description = models.CharField(max_length=300)
    gallery = models.ForeignKey(
        "galleries.gallery",
        on_delete=models.SET_NULL,
        null=True,
        related_name="videos",
    )
