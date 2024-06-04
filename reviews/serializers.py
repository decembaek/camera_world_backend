from rest_framework import serializers

from .models import Review


class GalleryReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["user", "payload", "rating"]
