import datetime

from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = models.DateTimeField(default=datetime.datetime.utcnow)
