from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    pass

class Task(models.Model):
    class Level(models.TextChoices):
        NORMAL = "NO", "普通"
        IMPORTANT = "IM", "重要"
    
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    level = models.CharField(max_length=2, choices=Level.choices, default=Level.NORMAL)
    photo = models.ImageField(upload_to="task/", null=True, blank=True)

    def __str__(self):
        return self.title