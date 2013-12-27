# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _
from apps.event.models import LanEvent


class SiteUser(AbstractUser):
    
    nickname = models.CharField(_(u'Nickname'), max_length=200)
    date_of_birth = models.DateField(_(u'Fødselsdag'),blank=False, null=True)
    phone = models.CharField(_(u'Telefonnummer'), max_length=16)
    skype = models.CharField(_(u'Skype'), max_length = 200,blank=True)
    steam = models.CharField(_(u'Steam'), max_length=200, blank=True)
    address = models.CharField(_(u'Adresse'), max_length=200)
    town = models.CharField(_(u'By'), max_length=200)
    zip_code = models.CharField(_(u'Postnummer'), max_length=200)
    country = models.CharField(_(u'Land'), max_length=200)
    image = models.ImageField(_(u'Bilde'), upload_to='users',max_length=150, blank=True)
    rfid = models.CharField(_(u'RFID'), max_length=100, blank=True)
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def get_user(self):
        return self 

    def get_email(self):
        return self.email

    def is_crew(self):
        current_event = LanEvent.objects.filter(current=True)[0]

        #check if the user is in a crew team
        if len(self.crewteam_set.all()) == 0:
            return False

        # if in crew team, is it for the current event?
        for crewteam in self.crewteam_set.all():
            if crewteam.event == current_event:
                return True
        return False

    def is_chief(self):
        if len(self.crew_set.all()) > 0:
            return True
        return False