from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # first_name = models.CharField(max_length=150, editable=False)
    # last_name = models.CharField(max_length=150, editable=False)
    username = None
    avatar = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=150)
    nickname = models.CharField(max_length=150, default="")
    email = models.EmailField(max_length=250, unique=True)
    camera = models.ManyToManyField(
        "cameras.camera",
        blank=True,
        related_name="owners",
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    is_email = models.BooleanField(default=False)
