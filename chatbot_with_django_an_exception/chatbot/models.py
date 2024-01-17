from django.db import models

class ChatMessage(models.Model):
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
