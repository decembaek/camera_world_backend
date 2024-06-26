# Generated by Django 4.2.13 on 2024-06-05 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("galleries", "0004_remove_gallery_place"),
        ("places", "0002_place_gallery"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="gallery",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="places",
                to="galleries.gallery",
            ),
        ),
    ]
