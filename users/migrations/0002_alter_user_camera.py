# Generated by Django 4.2.13 on 2024-05-25 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cameras", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="camera",
            field=models.ManyToManyField(
                blank=True, related_name="owners", to="cameras.camera"
            ),
        ),
    ]
