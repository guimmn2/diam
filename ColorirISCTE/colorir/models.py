from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    title = models.CharField(max_length=20)
    image = models.ImageField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    pub_data = models.DateTimeField('Post date')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    pub_data = models.DateTimeField()
