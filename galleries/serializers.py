from rest_framework import serializers

from medias.serializers import PhotoSerializer, VideoSerializer
from users.serializers import TinyUserSerializer
from reviews.serializers import GalleryReviewSerializer

from .models import Gallery


class GalleryListSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = [
            "id",
            "photos",
            "videos",
        ]


class GalleryDetailSerializer(serializers.ModelSerializer):
    photo_grapher = TinyUserSerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    reviews = GalleryReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = [
            "id",
            "title",
            "content",
            "photo_grapher",
            "camera",
            "place",
            "photos",
            "videos",
            "reviews",
        ]


class GalleryMakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = "__all__"
