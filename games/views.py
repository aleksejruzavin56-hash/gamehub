from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from games import models


# Create your views here.
def game_list(request):
    games = models.Game.objects.all()
    return render(request, 'index.html', {'games': games})

def top_games(request):
    games = models.Game.objects.order_by('-raing')[:5]
    return render(request, 'top_game.html', {'games': games})
def game_detail(request, id):
    games = models.Game.objects.filter(pk=id)
    if games.count() == 0:
        return render(request, '404.html')
    return render(request, 'game_detail.html', {'game': games[0]})