from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Article(models.Model):
    """Модель для хранения статей"""
    title = models.CharField(max_length=200)
    preview = models.TextField(max_length=200, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='static/blog', null=True, blank=True)
    cover = models.ImageField(upload_to='static/blog', null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Модель для хранения комментариев к статьям"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}_{self.article.title}"
