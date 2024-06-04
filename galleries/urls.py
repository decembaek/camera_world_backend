from django.urls import path

from . import views

urlpatterns = [
    path("", views.Galleries.as_view()),
    path("<int:gallery_id>", views.GalleryDetail.as_view()),
]
