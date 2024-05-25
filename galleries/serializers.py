from rest_framework import serializers

from medias.serializers import PhotoSerializer, VideoSerializer
from users.serializers import TinyUserSerializer

from .models import Gallery


class GalleryListSerializer(serializers.ModelSerializer):
    grapher = TinyUserSerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = [
            "title",
            "content",
            "grapher",
            "camera",
            "place",
            "photos",
            "videos",
        ]
