from django.urls import path

from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("activate/<uidb64>/<token>", views.ActivateView.as_view(), name="activate"),
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("log-out", views.LogOut.as_view()),
    path("camera", views.MyCamera.as_view()),
    path(
        "reset-password",
        views.PasswordResetAPIView.as_view(),
        name="password_reset_request",
    ),
    path(
        "reset-password/<uidb64>/<token>",
        views.PasswordResetConfirmAPIView.as_view(),
        name="password_reset_confirm",
    ),
    path("find-email", views.FindEmail.as_view()),
    # path("github", views.GithubLogIn.as_view()),
    # path("kakao", views.KakaoLogIn.as_view()),
    # path("@<str:username>", views.PublicUser.as_view()),
]
