# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from apps.crew.models import Crew

# Create your models here.


class Item(models.Model):

    stat = (
        (0, u'På lager'),
        (1, u'Sjekket ut'),
    )

    name = models.CharField(_(u'Navn'), max_length=60)
    quantity = models.IntegerField(_(u'Antall'))
    location = models.CharField(_('Lokasjon'), max_length=40)
    box = models.CharField(_('Boks'), max_length=40)
    description = models.TextField(_('Beskrivelse'))
    status = models.SmallIntegerField(_(u'Status'), choices=stat, default=0)
    owner = models.ForeignKey(Crew)

    def __unicode__(self):
        return self.name
