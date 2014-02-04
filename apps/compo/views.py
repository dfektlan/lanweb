# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from apps.event.models import LanEvent
from apps.compo.models import Game, Tournament, Participant, Team
from django.contrib import messages
from django.core.urlresolvers import reverse

LATEST_EVENT = LanEvent.objects.filter(current=True)[0]

def overview(request):
    all_games = Game.objects.all()
    all_tournaments = Tournament.objects.filter(event=LATEST_EVENT)
    tournament_dict = {}
    for g in all_games:
        tournament_dict[g] = all_tournaments.filter(game=g)
    return render(request, 'compo/overview.html', {'tournaments':tournament_dict, 'all_games':all_games})


def tournament(request, tournament_id=None):
    tour = get_object_or_404(Tournament, pk=tournament_id)
    participants = Participant.objects.filter(tournament=tournament_id)
    return render(request, 'compo/tournament.html', {'tournament': tour, 'participants': participants})


def register_to_tournament(request, tournament_id=None):
    tour = get_object_or_404(Tournament, pk=tournament_id)
    if not request.user.is_authenticated():
        messages.error(request, u'You most log in to register for a tournament')
    elif tour.has_participant(request.user):
        messages.error(request, u'You are already signed up for this tournament')
    else:
        make_participant(request.user, tour)
    return redirect('tournament', tournament_id)


def make_participant(user, tour):
    p = Participant()
    p.user = user
    p.tournament = tour
    p.save()

# OBS! Sjekk innlogging før registrering av team
