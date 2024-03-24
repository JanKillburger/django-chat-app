from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
  pass

class Chat(models.Model):
  created_at = models.DateTimeField(default=timezone.now)

class Message(models.Model):
  text = models.CharField(max_length=500)
  created_at = models.DateField(default=date.today)
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author_message_set")
  receiver =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)