from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import game_list, top_games, game_detail

urlpatterns = [path("top_games", top_games, name='top_games'),
                path("game_detail/<int:id>", game_detail, name='game_detail'),
               path("", game_list, name='game_list'),]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

