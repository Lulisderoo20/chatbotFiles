from django.db import models


class ChatMessage(models.Model):
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.timestamp.isoformat()} - {self.message[:50]}"
