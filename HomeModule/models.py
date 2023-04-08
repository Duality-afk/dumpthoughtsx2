from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    postkey = models.CharField(max_length=150, default=0)

class userProfile(models.Model):
    profile_username = models.CharField(max_length=150)
    status = models.CharField(max_length=1000, default="False")
    key = models.CharField(max_length=150)
    
    