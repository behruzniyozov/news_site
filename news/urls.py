from django.urls import path
from news.api_endpoints import *

urlpatterns = [
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news-detail'),
    path('news/create/', NewsCreateView.as_view(), name='news-create'),
    path('news/update/<slug:slug>/', NewsUpdateView.as_view(), name='news-update'),
    path('news/delete/<slug:slug>/', NewsDeleteView.as_view(), name='news-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/update/<slug:slug>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/delete/<slug:slug>/', CategoryDeleteView.as_view(), name='category-delete'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]