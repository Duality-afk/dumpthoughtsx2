from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    senderkey = models.CharField(max_length=10000000,default=0)
    receiverkey = models.CharField(max_length=100000,default=0)


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    userkey = models.CharField(max_length=1000000,default=0)


class openchat(models.Model):
    senderkey = models.CharField(max_length=100000)
    receiverkey = models.CharField(max_length=100000)
    
