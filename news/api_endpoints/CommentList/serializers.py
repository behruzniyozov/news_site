from rest_framework import serializers
from news.models import Comment, News

class CommentListSerializer(serializers.ModelSerializer):
    news = serializers.PrimaryKeyRelatedField(
        queryset=News.objects.all(),
        write_only=True,
        required=True
    )
    
    class Meta:
        model = Comment
        fields = ['id', 'news', 'content', 'created_at', 'news_id','user_id']
        read_only_fields = ['created_at', 'updated_at']
    
