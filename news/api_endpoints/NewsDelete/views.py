from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from news.models import News


class NewsDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, news_id):
        try:
            news_instance = News.objects.get(id=news_id)
            news_instance.delete()
            return Response({'message': 'News article deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except News.DoesNotExist:
            return Response({'error': 'News article not found'}, status=status.HTTP_404_NOT_FOUND)