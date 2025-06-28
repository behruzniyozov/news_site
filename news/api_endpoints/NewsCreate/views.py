from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from .serializers import NewsCreateSerializer
from news.models import News

class NewsCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = NewsCreateSerializer(data=request.data)
        if serializer.is_valid():
            news_instance = serializer.save()
            return Response({
                'message': 'News article created successfully',
                'news_id': news_instance.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)