# Generated by Django 4.2.13 on 2024-05-29 07:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]
