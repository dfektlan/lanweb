# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from apps.event.models import LanEvent


class Crew(models.Model):
    name = models.CharField(_(u'Crewnavn'), max_length=30)
    description = models.TextField(_(u'Beskrivelse'))
    date = models.DateTimeField(_(u'Dato'), editable=False, auto_now_add=True)
    chief = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, blank=True)

    def __unicode__(self):
        return self.name


class CrewMember(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    credit = models.IntegerField(default=0)
    event = models.ForeignKey(LanEvent, null=False)

    def __unicode__(self):
        return "Crew: " + self.user.first_name + " " + self.user.last_name


class CrewTeam(models.Model):
    crew = models.ForeignKey(Crew, null=False)
    name = models.CharField(_(u'Navn'), max_length=30)
    description = models.TextField(_(u'Beskrivelse'))
    date = models.DateTimeField(_(u'Dato'), editable=False, auto_now_add=True)
    members = models.ManyToManyField(CrewMember, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Application(models.Model):


    stat = (
    (0, u'PENDING'),
    (1, u'APPROVED'),
    (2, u'DECLINED')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, editable=False)
    about = models.TextField(_(u'Om meg'))
    why = models.TextField(_(u'Hvorfor meg'))
    license = models.CharField(_(u'Førerkort'), max_length=200)
    status = models.SmallIntegerField(_(u'Status'), choices=stat, default=0)
    date = models.DateTimeField(_(u'Dato'), editable=False, auto_now_add=True)
    crew = models.ForeignKey(CrewTeam)
    #crew = models.SmallIntegerField(_(u'Crew'), choices=crews, blank=False, default=0)
    cv = models.URLField(_(u'CV'), max_length=200, blank=True)
    event = models.ForeignKey(LanEvent)
    
    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name

    class Meta:
        get_latest_by = 'date'
