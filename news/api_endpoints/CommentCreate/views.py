from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from news.models import Comment
from .serializers import CommentCreateSerializer

class CommentCreateView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            comment_instance = serializer.save(user=request.user)
            return Response({
                'message': 'Comment created successfully',
                'comment_id': comment_instance.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)