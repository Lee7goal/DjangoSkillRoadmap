from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TodoModel(models.Model):
    short_text = models.CharField(max_length=100)
    long_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.short_text + "         by " + self.create_by.username

    class Meta:
        ordering = ['created_at']
