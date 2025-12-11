from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks',on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} - {'Done' if self.status else 'Pending'}"
    