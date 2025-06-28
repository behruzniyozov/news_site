from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from news.models import Category
from .serializers import CategoryUpdateSerializer

class CategoryUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, category_id):
        try:
            category_instance = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategoryUpdateSerializer(category_instance, data=request.data, partial=True)
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response({
                'message': 'Category updated successfully',
                'category_id': updated_category.id
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)