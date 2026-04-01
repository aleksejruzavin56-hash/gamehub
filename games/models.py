from datetime import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ForeignKey("GameGenre", on_delete=models.CASCADE, null = True, blank = True)
    raing = models.IntegerField()
    date = models.DateField(default=timezone.now())
    def __str__(self):
        return self.title
class GameGenre(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
class GameInfo(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    description = models.TextField()
    steam_url = models.URLField()
    image = models.ImageField(upload_to="games/")