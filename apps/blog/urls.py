from django.urls import path
from .views import BlogView, BlogSingleView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('blogsingle/<int:article_id>', BlogSingleView.as_view(), name='blogsingle'),
    path('blogsingle', BlogSingleView.as_view(), name='blogSingle')
]