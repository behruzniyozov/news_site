from rest_framework import serializers
from news.models import Comment, News

class CommentCreateSerializer(serializers.ModelSerializer):
    news= serializers.PrimaryKeyRelatedField(
        queryset=News.objects.all(),
        write_only=True,
        required=True
    )
    class Meta:
        model = Comment
        fields = ['news', 'content']
        read_only_fields = ['created_at', 'updated_at']

        