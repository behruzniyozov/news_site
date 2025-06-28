from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from news.models import Comment
from .serializers import CommentListSerializer

class CommentListView(APIView):
    permission_classes = []

    def get(self, request):
        comments_queryset = Comment.objects.all()
        serializer = CommentListSerializer(comments_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

