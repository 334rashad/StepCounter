from django.db import models
from apps.challenges.models import Challenge


class Team(models.Model):
    name = models.CharField(max_length=255)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name="teams")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.challenge.name})"