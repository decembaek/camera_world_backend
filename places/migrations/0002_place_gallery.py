# Generated by Django 4.2.13 on 2024-06-05 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("galleries", "0004_remove_gallery_place"),
        ("places", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="place",
            name="gallery",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="galleries.gallery",
            ),
            preserve_default=False,
        ),
    ]
