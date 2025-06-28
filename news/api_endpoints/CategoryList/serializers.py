from rest_framework import serializers
from news.models import Category

class CategoryListSerializer(serializers.ModelSerializer):
    news_ids = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True, source='news.all'
    )

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'news_ids']
        read_only_fields = ['id', 'slug', 'news_ids']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['news_ids'] = [news.id for news in instance.news.all()]
        return representation