from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("이메일 필드가 필요합니다")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    # first_name = models.CharField(max_length=150, editable=False)
    # last_name = models.CharField(max_length=150, editable=False)
    username = None
    avatar = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=150)
    nickname = models.CharField(max_length=150, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=250, unique=True)
    camera = models.ManyToManyField(
        "cameras.camera",
        blank=True,
        related_name="owners",
    )

    # objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    is_email = models.BooleanField(default=False)
    is_profile = models.BooleanField(default=False)
