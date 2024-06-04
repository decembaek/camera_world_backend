from rest_framework import serializers

from galleries.models import Gallery

from .models import User

# from galleries.serializers import MyGallerySerializer


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "nickname", "camera", "avatar"]


# 마이페이지 갤러리 보기
class MyGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class MakeUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password"]


class ProfileUserSerializer(serializers.ModelSerializer):
    galleries = MyGallerySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "avatar",
            "name",
            "nickname",
            "camera",
            "galleries",
            "email",
            "is_email",
        ]
