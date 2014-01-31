# -*- coding: utf-8 -*-
from django.db import models
from apps.event.models import LanEvent
from django.conf import settings
from django.utils.translation import ugettext as _

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
        (2, u'IN PROGRESS'),
        (3, u'FINISHED')
    )

    title = models.CharField(_(u'Tittel'), max_length=30)
    description = models.TextField(_(u'Beskrivelse'))
    open = models.BooleanField(_(u'påmelding'), default=False)
    status = models.SmallIntegerField(_(u'Status'), choices=stat, default=0)
    use_teams = models.BooleanField(_(u'Lag?'), default=False)
    max_participants = models.IntegerField(_(u'Max deltagere'))
    max_pr_team = models.IntegerField(_(u'Max pr. lag'))
    reg_start = models.DateTimeField(_(u'Påmeldingsstart'))
    reg_stop = models.DateTimeField(_(u'Påmeldingsslutt'))
    start_time = models.DateTimeField(_(u'Starttid'))
    stop_time = models.DateTimeField(_(u'Sluttid'))
    event = models.ForeignKey(LanEvent)
    game = models.ForeignKey(Game)

    def status_text(self):
        return self.status[1]

    def __unicode__(self):
        return self.title

class Team(models.Model):
    title = models.CharField(_(u'Lagnavn'), max_length=30)
    teamleader = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="new_teamleader")
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True)

    def __unicode__(self):
        return self.title

class Participant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True)
    tournament = models.ForeignKey(Tournament)

