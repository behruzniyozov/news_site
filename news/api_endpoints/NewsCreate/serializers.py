from rest_framework import serializers
from news.models import News
from common.models import MediaFile

class NewsCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=MediaFile.objects.all()),
        required=False,
        allow_empty=True
    )
    
    class Meta:
        model = News
        fields = [
            'title',
            'slug',
            'authors',
            'categories',
            'tags',
            'default_image',
            'images',
            'is_active',
            'content'
            'is_public'
        ]
        read_only_fields = ['view_count', 'liked_by', 'published_date']
        lookup_field = 'slug'
    
    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        news_instance = News.objects.create(**validated_data)
        news_instance.images.set(images_data)
        return news_instance