from django.db import models
from django.conf import settings
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20)
    descriptions = models.TextField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)