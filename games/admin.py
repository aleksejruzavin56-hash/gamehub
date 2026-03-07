from django.contrib import admin

from games.models import Game, GameGenre

# Register your models here.
admin.site.register(Game)
admin.site.register(GameGenre)