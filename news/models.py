from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='news_articles', blank=True)
    categories = models.ManyToManyField('news.Category', related_name='news_items', blank=True)
    tags = models.ManyToManyField('news.Tag', related_name='news_items', blank=True)
    default_image = models.ImageField(upload_to='news/default_images/', blank=True, null=True)
    images = models.ManyToManyField('common.MediaFile', related_name='news_articles', blank=True)
    is_active = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_news', blank=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-published_date']


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    # Removed ManyToMany to News to avoid conflict with News.tags
    # All access should be via News.tags

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    # Removed ManyToMany to News to avoid conflict with News.categories

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(max_length=500)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    news_id = models.ForeignKey('News', related_name='comments', on_delete=models.CASCADE)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.id} by {self.user_id} on {self.news_id}"
