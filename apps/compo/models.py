# -*- coding: utf-8 -*-
from django.db import models
from apps.event.models import LanEvent
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


class Game(models.Model):
    title = models.CharField(_(u'Tittel'), max_length=30)
    description = models.TextField(_(u'Beskrivelse'))
    image = models.ImageField(_(u'Bilde'), upload_to='compo', blank=True)

    def __unicode__(self):
        return self.title


class Tournament(models.Model):
    stat = (
        (0, u'OPEN'),
        (1, u'CLOSED'),
        (2, u'ABOUT_TO_START'),
        (3, u'IN_PROGRESS'),
        (4, u'FINISHED')
    )

    title = models.CharField(_(u'Tittel'), max_length=30)
    description = models.TextField(_(u'Beskrivelse'))
    status = models.SmallIntegerField(_(u'Status'), choices=stat, default=0)
    open = models.BooleanField(_(u'Påmelding kreves?'), default=False)
    max_participants = models.IntegerField(_(u'Max deltagere'), blank=True, default=0)
    use_teams = models.BooleanField(_(u'Bruk lag?'), default=False)
    max_pr_team = models.IntegerField(_(u'Max pr. lag (uten lagleder)'))
    reg_start = models.DateTimeField(_(u'Påmeldings- start'))
    reg_stop = models.DateTimeField(_(u'Påmeldings- slutt'))#, validators=[MinValueValidator(reg_start)])
    start_time = models.DateTimeField(_(u'Turnerings- start'))
    stop_time = models.DateTimeField(_(u'Turnerings- slutt'))
    event = models.ForeignKey(LanEvent)
    game = models.ForeignKey(Game)
    challonge_url = models.CharField(_(u'Challonge URL'), max_length=30)

    class Meta:
        ordering = ['status']

    def set_status(self):
        now = timezone.localtime(timezone.now())
        if self.reg_start > now: # registrering ikke åpnet
            self.status = 1
        if self.reg_start < now: # registrering åpnet
            self.status = 0
        if self.reg_stop < now and self.start_time > now: # registrering lukket og turnering ikke startet
            self.status = 2
        if self.reg_stop < now and self.start_time < now: # registrering lukket og turnering startet
            self.status = 3
        if self.stop_time < now:
            self.status = 4
        self.save()

    def get_participants(self):
        participants = Participant.objects.filter(tournament=self)
        users = []
        teams = []
        for p in participants:
            if self.use_teams:
                teams.append(p.team)
            else:
                users.append(p.user)
        return teams if self.use_teams else users

    def __unicode__(self):
        return self.title


class Team(models.Model):
    title = models.CharField(_(u'Lagnavn'), max_length=30)
    teamleader = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="is_teamleader")
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="is_teammember")

    def __unicode__(self):
        return self.title


class Participant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True)
    tournament = models.ForeignKey(Tournament)

    def __unicode__(self):
        return self.user.nickname if self.user else self.team.title


#Validators for admin (example)
def validate_status(value):
    if value % 2 != 0:
        raise ValidationError(u'%s is not an even number' % value)
