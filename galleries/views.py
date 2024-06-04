from django.db import transaction

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

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

    def post(self, request):
        if request.user.is_email:
            serializer = serializers.GalleryMakeSerializer(data=request.data)
            if serializer.is_valid():
                place = request.data.get("place")
            else:
                return Response(serializer.errors)
        else:
            return Response(
                {"erorr": "로그인 하거나 계정 인증을 완료해야 합니다."},
                status=status.HTTP_403_FORBIDDEN,
            )


class GalleryDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_gallery(self, pk):
        try:
            return Gallery.objects.get(pk=pk)
        except Gallery.DoesNotExist:
            return None

    def get(self, request, gallery_id):
        gallery = self.get_gallery(pk=gallery_id)
        if gallery is None:
            return Response(
                {"error": "Gallery가 없습니다"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = serializers.GalleryDetailSerializer(gallery)

        return Response(serializer.data)
