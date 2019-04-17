from django.db import models
from django.contrib.auth.models import User


class Snippet(models.Model):
    name=models.CharField(max_length=100)
    body=models.TextField()

    def __str__(self):
        return self.name
