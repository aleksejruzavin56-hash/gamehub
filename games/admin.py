from django.contrib import admin
from django.contrib.auth.models import User

from games.models import Game, GameGenre, GameInfo

# Register your models here.
admin.site.register(Game)
admin.site.register(GameGenre)
admin.site.register(GameInfo)