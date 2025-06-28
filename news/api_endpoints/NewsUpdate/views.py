from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import NewsUpdateSerializer
from news.models import News


class NewsUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, news_id):
        try:
            news_instance = News.objects.get(id=news_id)
        except News.DoesNotExist:
            return Response({'error': 'News article not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = NewsUpdateSerializer(news_instance, data=request.data, partial=True)
        if serializer.is_valid():
            updated_news_instance = serializer.save()
            return Response({
                'message': 'News article updated successfully',
                'news_id': updated_news_instance.id
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)