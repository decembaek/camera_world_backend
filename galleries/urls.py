from django.urls import path

from . import views

urlpatterns = [
    path("", views.Galleries.as_view()),
]
