from django.db import models
class Testimony(models.Model):
    text = models.TextField(max_length=200, null=True, blank=True)
    author = models.TextField(max_length=200, null=True, blank=True)
    profession = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='static/avatars', null=True, blank=True)

    def __str__(self):
        return self.author

