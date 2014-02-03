from django.shortcuts import render, get_object_or_404
from apps.event.models import LanEvent
from apps.compo.models import Game, Tournament, Participant, Team


LATEST_EVENT = LanEvent.objects.filter(current=True)[0]

def overview(request):
    all_games = Game.objects.all()
    all_tournaments = Tournament.objects.filter(event=LATEST_EVENT)
    tournament_dict = {}
    for g in all_games:
        tournament_dict[g] = all_tournaments.filter(game=g)
    return render(request, 'compo/overview.html', {'tournaments':tournament_dict, 'all_games':all_games})

def tournament(request, tournament_id=None):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    participants = Participant.objects.filter(tournament=tournament_id)
    return render(request, 'compo/tournament.html', {'tournament':tournament, 'participants':participants})