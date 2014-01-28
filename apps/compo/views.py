from django.shortcuts import render
from apps.event.models import LanEvent
from apps.compo.models import Game,Tournament,Participant,Team

LATEST_EVENT = LanEvent.objects.filter(current=True)[0]

def overview(request):
    all_games = Game.objects.all()
    all_tournaments = Tournament.objects.filter(event=LATEST_EVENT)
    tournament_dict = {}
    for g in all_games:
        tournament_dict[g] = all_tournaments.filter(game=g)
    return render(request, 'compo/overview.html', {'tournaments':tournament_dict, 'all_games':all_games})