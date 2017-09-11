from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def rating(self):
        """
        Returns the rating for the current Post.
        :rtype: int 
        """
        positive = PostRating.objects.filter(post=self, positive=True).count()
        negative = PostRating.objects.filter(post=self, positive=False).count()

        return positive - negative


class PostRating(models.Model):
    positive = models.BooleanField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model())
