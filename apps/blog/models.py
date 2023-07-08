from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    preview = models.TextField(max_length=200, null=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='static/blog', null=True, blank=True)
    cover = models.ImageField(upload_to='static/blog', null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
