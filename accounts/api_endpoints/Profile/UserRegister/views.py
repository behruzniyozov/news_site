from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import *

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class UserRegisterRequestView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=UserRegisterRequestSerializer,
        responses={201: "User registered successfully", 400: "Invalid data"}
    )
    def post(self, request):
        serializer = UserRegisterRequestSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User registered successfully",
                "user_id": user.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserRegisterConfirmView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        request_body=UserRegisterVerifySerializer,
        responses={200: "User registration confirmed", 400: "Invalid token or user already registered"}
    )
    def post(self, request):
        serializer = UserRegisterVerifySerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User registration confirmed",
                "user_id": user.id
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)