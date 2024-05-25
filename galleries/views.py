from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from . import serializers

from .models import Gallery


class Galleries(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_galleries = Gallery.objects.all()
        serializer = serializers.GalleryListSerializer(
            all_galleries,
            many=True,
        )
        return Response(serializer.data)
