from rest_framework import serializers
from .models import Photo, Video


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ["file", "description"]


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ["file", "description"]
