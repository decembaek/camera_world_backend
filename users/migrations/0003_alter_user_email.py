# Generated by Django 4.2.13 on 2024-05-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_camera"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(editable=False, max_length=250, unique=True),
        ),
    ]
