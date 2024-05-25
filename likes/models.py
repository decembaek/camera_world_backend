from django.db import models
from common.models import CommonModel

# Create your models here.


class Like(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )
    gallery = models.ForeignKey(
        "galleries.gallery",
        on_delete=models.CASCADE,
        related_name="gallery",
    )
