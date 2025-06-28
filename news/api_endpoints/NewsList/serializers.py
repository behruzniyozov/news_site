from rest_framework import serializers
from news.models import News
from common.models import MediaFile

class NewsListSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=MediaFile.objects.all()),
        required=False,
        allow_empty=True
    )
    
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'slug',
            'authors',
            'categories',
            'tags',
            'default_image',
            'images',
            'is_active',
            'view_count',
            'liked_by',
            'content',
            'published_date'
            'is_public'
        ]
        read_only_fields = ['view_count', 'liked_by', 'published_date']
        lookup_field = 'slug'