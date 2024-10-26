from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField("Tag", related_name="posts")

class Tag(models.Model):
    name = models.CharField(max_length=30)
