# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _
from apps.crew.models import CrewShift

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
