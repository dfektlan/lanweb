# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _
from apps.event.models import LanEvent


class SiteUser(AbstractUser):
    
    nickname = models.CharField(_(u'Brukernavn'), max_length=200)
    date_of_birth = models.DateField(_(u'Fødselsdag'),blank=False, null=True)
    phone = models.CharField(_(u'Telefonnummer'), max_length=16)
    skype = models.CharField(_(u'Skype'), max_length = 200,blank=True, null=True)
    steam = models.CharField(_(u'Steam'), max_length=200, blank=True, null=True)
    address = models.CharField(_(u'Adresse'), max_length=200)
    town = models.CharField(_(u'By'), max_length=200)
    zip_code = models.CharField(_(u'Postnummer'), max_length=200)
    country = models.CharField(_(u'Land'), max_length=200)
    image = models.ImageField(_(u'Bilde'), upload_to='users',max_length=150, blank=True)
    rfid = models.CharField(_(u'RFID'), max_length=100, blank=True, unique=True)
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def get_user(self):
        return self 

    def get_email(self):
        return self.email

    def is_crew(self, event):
        eventObj = LanEvent.objects.get(shortname=event)

        #check if the user is in a crew team
        if len(self.crewmember_set.all()) == 0:
            return False

        # if in crew team, is it for the current event?
        for member in self.crewmember_set.all():
            if member.event == eventObj:
                return True
        return False

    def is_chief(self):
        if len(self.crew_set.all()) > 0:
            return True
        return False

    def setNameNotRetard(self):

        def setFirstCap(string):
            string = string[:1].upper() + string[1:].lower()
            return string
        
        print self.first_name + " " + self.last_name
        self.first_name = " ".join(map(setFirstCap, self.first_name.split(" ")))
        self.last_name = " ".join(map(setFirstCap, self.last_name.split(" ")))
        self.save()

        return True
