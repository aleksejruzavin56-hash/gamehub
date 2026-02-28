from datetime import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    raing = models.IntegerField()
    date = models.DateField(default=timezone.now())
    def __str__(self):
        return self.title