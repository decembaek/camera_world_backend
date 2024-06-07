from rest_framework import serializers

from medias.serializers import PhotoSerializer, VideoSerializer
from users.serializers import TinyUserSerializer
from reviews.serializers import GalleryReviewSerializer
from places.serializers import PlaceGallerySerializer

from .models import Gallery

import random


class GalleryListSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()
    videos = VideoSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = [
            "id",
            "photo",
            "videos",
        ]

    def get_photo(self, obj):

        photos = obj.photos.all()
        if photos.exists():
            random_photo = random.choice(photos)
            return PhotoSerializer(random_photo).data
        return None


class GalleryDetailSerializer(serializers.ModelSerializer):
    photo_grapher = TinyUserSerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    reviews = GalleryReviewSerializer(many=True, read_only=True)
    places = PlaceGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = [
            "id",
            "title",
            "content",
            "photo_grapher",
            "camera",
            "photos",
            "videos",
            "reviews",
            "places",
        ]

    # def get_places(self, obj):
    #     print(obj)


class GalleryMakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gallery
        fields = ["title", "content"]
