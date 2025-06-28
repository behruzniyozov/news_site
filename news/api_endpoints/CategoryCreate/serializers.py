from rest_framework import serializers
from news.models import Category

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'news_ids']
        read_only_fields = ['slug']

    def create(self, validated_data):
        category_instance = Category.objects.create(**validated_data)
        return category_instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.news_ids.set(validated_data.get('news_ids', instance.news_ids.all()))
        instance.save()
        return instance