from django.db import transaction

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from medias.models import Photo, Video

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
                photos = request.data.get("photos")
                videos = request.data.get("videos")
                camera = request.data.get("camera")

                if photos is None and videos is None:
                    return Response(
                        {"error": "업로드한 파일이 없습니다"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
                try:
                    with transaction.atomic():
                        gallery = serializer.save(photo_grapher=request.user)
                        # Photos 추가
                        if photos:
                            for photo_data in photos:
                                Photo.objects.create(
                                    file=photo_data["file"],
                                    description=photo_data.get("description", ""),
                                    gallery=gallery,
                                )

                        # Videos 추가
                        if videos:
                            for video_data in videos:
                                Video.objects.create(
                                    file=video_data["file"],
                                    description=video_data.get("description", ""),
                                    gallery=gallery,
                                )
                        serializer = serializers.GalleryMakeSerializer(gallery)
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                except:
                    return Response(
                        {"error": "갤러리 저장에 실패하였습니다"},
                        status=status.HTTP_404_NOT_FOUND,
                    )
            else:
                return Response(serializer.errors)
        else:
            return Response(
                {"erorr": "로그인 하거나 계정 인증을 완료해야 합니다."},
                status=status.HTTP_403_FORBIDDEN,
            )


# {
#     "title": "post title",
#     "content": "post content"
# }
# {
# {
#     "title": "post title3",
#     "content": "post content3",
#     "photos": [
#         {
#             "file": "https://www.hyundai.com/contents/repn-car/side-45/main-the-new-tucson-hybrid-45side.png",
#             "description": "haha"
#         },
#         {
#             "file": "https://www.hyundai.com/contents/repn-car/side-45/main-the-new-tucson-hybrid-45side.png",
#             "description": "haha"
#         }
#     ],
#  "videos": [
#         {
#             "file": "https://www.hyundai.com/contents/repn-car/side-45/main-the-new-tucson-hybrid-45side.png",
#             "description": "haha"
#         },
#         {
#             "file": "https://www.hyundai.com/contents/repn-car/side-45/main-the-new-tucson-hybrid-45side.png",
#             "description": "haha"
#         }
#     ]
# }


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
