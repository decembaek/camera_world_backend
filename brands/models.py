from django.db import models


# Create your models here.
class Brand(models.Model):
    nanme = models.CharField(max_length=150)
    description = models.TextField()
