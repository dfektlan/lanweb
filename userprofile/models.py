# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext as _

class SiteUser(AbstractUser):
    nickname = models.CharField(_(u'Nickname'), max_length=200)
    date_of_birth = models.DateField(_(u'Fødselsdag'))
    phone = models.CharField(_(u'Telefonnummer'), max_length=16)
    skype = models.CharField(_(u'Skype'), max_length = 200,blank=True)
    steam = models.CharField(_(u'Steam'), max_length=200, blank=True)
    address = models.CharField(_(u'Adresse'), max_length=200)
    town = models.CharField(_(u'By'), max_length=200)
    zip_code = models.CharField(_(u'Postnummer'), max_length=200)
    country = models.CharField(_(u'Land'), max_length=200)
    chief = models.BooleanField(_(u'Sjef'), null=False, default=False)
    position = models.CharField(_(u'Posisjon'), max_length=200, blank=True)
    objects = UserManager()
    image = models.ImageField(_(u'Bilde'), upload_to='users',max_length=150, blank=True)
    
    def __unicode__(self):
        return (self.first_name + " " + self.last_name)

    def get_user(self):
        return self 
