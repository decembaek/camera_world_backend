from django.db import models
from common.models import CommonModel


# Create your models here.
class Gallery(CommonModel):
    title = models.CharField(max_length=200)
    content = models.TextField(default="")
    photo_grapher = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    camera = models.ForeignKey(
        "cameras.camera",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    place = models.ForeignKey(
        "places.place",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.photo_grapher}_{self.title}_ID_{self.id}"
