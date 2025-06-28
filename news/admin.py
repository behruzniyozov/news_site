from django.contrib import admin
from .models import News, Category, Comment, Tag  # Add other models as needed

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "is_active", "published_date")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("is_published", "is_active", "categories", "tags")
    search_fields = ("title", "content")
    filter_horizontal = ("authors", "categories", "tags", "liked_by", "images")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "news_id", "created_at")
    search_fields = ("content",)
    list_filter = ("created_at",)
