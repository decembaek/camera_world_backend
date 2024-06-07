from django.contrib.auth import authenticate, login, logout
from django.db import transaction

from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from . import serializers
from .models import User


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.ProfileUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Users(APIView):

    @transaction.atomic
    def post(self, request):
        password = request.data.get("password")
        email = request.data.get("email")
        if not password:
            return Response(
                {"error": "패스워드를 입력해주세요"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if not email:
            return Response(
                {"error": "이메일을 입력해주세요"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "이미 존재하는 이메일입니다"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = serializers.MakeUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.is_active = False
            user.save()

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            activation_link = f"{settings.FRONTEND_URL}/user/activate/{uid}/{token}"
            context = {"user": user.email, "url": activation_link, "form": "인증"}
            html_contents = render_to_string("account_mail.html", context)
            mail_subject = "[CW] 계정 인증을 완료해주세요."
            text_contents = "계정 인증을 위한 메세지 입니다."
            email = EmailMultiAlternatives(
                mail_subject,
                text_contents,
                settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
            )
            email.attach_alternative(html_contents, "text/html")
            email.send()

            # email_body = f"안녕하세요 {user.email}님,\n아래 링크를 눌러 이메일 인증을 완료하세요.\n{activation_link}"
            # send_mail(
            #     "계정을 활성화 하세요.",
            #     email_body,
            #     settings.DEFAULT_FROM_EMAIL,
            #     [user.email],
            #     fail_silently=False,
            # )

            # login(request=request, user=user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# {"email": "tmdrb123@gmail.com", "password": "0000"}
class ActivateView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.is_email = True
            user.save()
            return Response(
                {"message": "Account activated successfully."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Invalid activation link."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        if not old_password or not new_password:
            return Response(
                {"error": "변경할 패스워드를 입력해주세요"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogIn(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        print(email)
        print(password)
        if not email or not password:
            return Response(
                {"error": "이메일과 비밀번호를 모두 입력해주세요."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = authenticate(
            request=request,
            email=email,
            password=password,
        )
        if user:
            login(request=request, user=user)
            return Response({"ok": "로그인 하였습니다"}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": "비밀번호가 틀렸습니다"}, status=status.HTTP_400_BAD_REQUEST
            )


class LogOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"ok": "로그아웃 되었습니다"})


class MyCamera(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = serializers.TinyUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PasswordResetAPIView(APIView):

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except:
            return None

    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response(
                {"error": "이메일을 입력해주세요"}, status=status.HTTP_400_BAD_REQUEST
            )

        user = self.get_user(email=email)
        if user is None:
            return Response(
                {"error": "이메일로 가입된 계정이 존재하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"{settings.FRONTEND_URL}/user/reset/{uid}/{token}/"

            context = {"user": user.email, "url": reset_link, "form": "찾기"}
            html_contents = render_to_string("account_mail.html", context)
            mail_subject = "[CW] 계정 찾기을 완료해주세요."
            text_contents = "계정 찾기을 위한 메세지 입니다."
            email = EmailMultiAlternatives(
                mail_subject,
                text_contents,
                settings.DEFAULT_FROM_EMAIL,
                to=[user.email],
            )
            email.attach_alternative(html_contents, "text/html")
            email.send()

        return Response(
            {"ok": "비밀번호 재설정 링크를 이메일로 보냈습니다"},
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmAPIView(APIView):
    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response(
                {"error": "유효하지 않은 링크입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if default_token_generator.check_token(user, token):
            new_password = request.data.get("new_password")
            if not new_password:
                return Response(
                    {"error": "새 비밀번호를 입력해주세요"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.set_password(new_password)
            user.save()
            return Response(
                {"message": "비밀번호가 성공적으로 재설정되었습니다."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "유효하지 않은 링크입니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class FindEmail(APIView):
    def get(self, request):
        print(request.data)
        serializer = serializers.FindUserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# {
#     "first_name" : "",
#     "last_name" : "",
#     "name" : "",
#     "nickname": ""
# }
