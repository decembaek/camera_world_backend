from django.contrib.auth import authenticate, login, logout
from django.db import transaction

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError

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
            user.save()
            serializer = serializers.MakeUserSerializer(user)
            login(request=request, user=user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# {"email": "tmdrb123@gmail.com", "password": "0000"}


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
