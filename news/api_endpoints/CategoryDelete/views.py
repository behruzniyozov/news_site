from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from news.models import Category

class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)