from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import NewsListSerializer
from news.models import News

class NewsListView(APIView):
    permission_classes = []

    def get(self, request):
        news_queryset = News.objects.all()
        serializer = NewsListSerializer(news_queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
