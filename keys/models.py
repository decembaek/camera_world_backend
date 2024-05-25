from django.db import models
from common.models import CommonModel

# Create your models here.


class Key(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    code = models.CharField(max_length=300)
