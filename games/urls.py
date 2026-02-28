from django.urls import path
from .views import game_list, top_games, game_detail

urlpatterns = [path("top_games", top_games, name='top_games'),
                path("game_detail/<int:id>", game_detail, name='game_detail'),
               path("", game_list, name='game_list'),]

