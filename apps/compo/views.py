# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from apps.event.models import LanEvent
from apps.compo.models import Game, Tournament, Participant, Team
from django.contrib import messages
from forms import RegisterTeamForm
from django.contrib.auth.decorators import login_required

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
    participants = tour.get_participants()
    is_participant = has_participant(tour, request.user)
    if request.POST:
        form = RegisterTeamForm(request.POST, request=request)
        if form.is_valid():
            make_team_participant(request, form, tour)
    else:
        form = RegisterTeamForm(request=request)
    return render(request, 'compo/tournament.html', {'tournament': tour, 'participants': participants,
                                                     'form': form, 'is_participant': is_participant})


def register_to_tournament(request, tournament_id=None):
    tour = get_object_or_404(Tournament, pk=tournament_id)
    if not request.user.is_authenticated():
        messages.error(request, u'You must log in to register for a tournament')
    elif has_participant(tour, request.user):
        messages.error(request, u'You are already signed up for this tournament')
    else:
        make_participant(request.user, tour)
        messages.success(request, u'You have successfully register for this tournament')
    return redirect('tournament', tournament_id)


def has_participant(tour, user):
    participants = tour.get_participants()
    if tour.use_teams:
        for p in participants:
            if user in p.members.all():
                return True
    else:
        for p in participants:
            if user == p:
                return True
    return False
    # participants = Participant.objects.filter(tournament=tournament_id)
    # is_participant = True if request.user in participants else False
    # for participant in participants:
    #     if request.user in participant.team.members.all():
    #         is_participant = True


def make_participant(user, tour):
    p = Participant()
    p.user = user
    p.tournament = tour
    p.save()


def make_team_participant(request, form, tour):
    team = Team()
    participant = Participant()
    team.teamleader = request.user
    team.title = form.cleaned_data['teamname']
    team.save()
    for user in form.cleaned_data['username']:
        team.members.add(user)
    team.save()
    participant.team = team
    participant.tournament = tour
    participant.save()
    messages.success(request, u'You have successfully registered your team for this tournament')


def check_user(request, tournament_id=None):
    if not request.user.is_authenticated():
        messages.error(request, u'You must log in to register for a tournament')
    return redirect('tournament', tournament_id)


def remove_participant(request, tournament_id=None):
    tour = get_object_or_404(Tournament, pk=tournament_id)
    participants = tour.get_participants()
    if tour.use_teams:
        for team in participants:
            if request.user in team.members.all():
                team.members.remove(request.user)
                messages.success(request, u'You was removed from the team')
    else:
        print participants
        participant = Participant.objects.get(user=request.user, tournament=tournament_id)
        participant.delete()
        print participants
        messages.success(request, u'You was unregistered from this tournament')
    return redirect('tournament', tournament_id)