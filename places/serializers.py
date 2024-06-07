from rest_framework import serializers


from .models import Place


class PlaceGallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ["id", "name", "address", "city", "country"]
