from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from news.models import News
from .serializers import NewsDetailSerializer

class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    permission_classes = []
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if not instance.is_public and not request.user.is_authenticated:
            return Response({'error': 'This news article is not public.'}, status=403)
        instance.view_count += 1
        instance.save(update_fields=['view_count'])
        return Response(serializer.data)