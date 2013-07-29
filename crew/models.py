# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from django.utils.translation import ugettext as _
from event.models import LanEvent

class Crew(models.Model):
    name = models.CharField(_(u'Crewnavn'), max_length=30)
    description = models.TextField(_(u'Beskrivelse'))
    
    def __unicode__(self):
        return (self.name)

class CrewGroup(models.Model):
    crew = models.ForeignKey(Crew)
    name = models.CharField(_(u'Crewgruppenavn'), max_length=30)
    description = models.TextField(_(u'Beskrivelse'))
    event = models.ForeignKey(LanEvent)
    
    def __unicode__(self):
        return (self.crew.name + ":" + self.name)

class CrewShift(models.Model):
    crewgroup = models.ForeignKey(CrewGroup)
    name = models.CharField(_(u'Skiftnavn'), max_length=30)
    description = models.TextField(_(u'Beskrivelse'))

    def __unicode__(self):
        return (self.crewgroup.event.name + " - " + self.crewgroup.crew.name + ":" + self.crewgroup.name + " " + self.name)

#class CrewWiki(models.Model):
    #Awesome shall be made
    #Keyet til hver crewgroup
    

class Application(models.Model):
    crews = (
    (0, u'Tech'),
    (1, u'Game'),
    (2, u'Kantine'),
    (3, u'Strøm'),
    (4, u'Logistikk'),
    (5, u'Sikkerhet'),
    )

    
    stat = (
    (0,'PENDING'),
    (1, 'APPROVED'), 
    (2, 'DECLINED')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, editable=False)
    about = models.TextField(_(u'Om meg'))
    why = models.TextField(_(u'Hvorfor meg'))
    license = models.CharField(_(u'Førerkort'), max_length=200)
    status = models.SmallIntegerField(_(u'Status'), choices=stat, default=0)
    date = models.DateTimeField(_(u'Dato'), editable=False, auto_now_add=True)
    crew = models.ForeignKey(CrewGroup)
    #crew = models.SmallIntegerField(_(u'Crew'), choices=crews, blank=False, default=0)
    cv = models.URLField(_(u'CV'), max_length=200, blank=True)
    
    def __unicode__(self):
        return (self.user.first_name + " " + self.user.last_name)

    class Meta:
        get_latest_by = 'date'
