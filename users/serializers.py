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
            "is_profile",
        ]


class FindUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "name", "nickname"]

    # def validate(self, data):
    #     if (
    #         not data.get("first_name")
    #         and not data.get("last_name")
    #         and not data.get("name")
    #     ):
    #         raise serializers.ValidationError("이름 작성란을 채워주세요")
    #     if not data.get("nickname"):
    #         raise serializers.ValidationError("닉네임을 작성해주세요")
    #     return data
