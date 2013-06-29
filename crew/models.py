# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group

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
    about = models.TextField()
    why = models.TextField()
    license = models.CharField(max_length=200)
    status = models.SmallIntegerField(choices=stat, default=0)
    date = models.DateTimeField(editable=False, auto_now_add=True)
    crew = models.SmallIntegerField(choices=crews)

    class Meta:
        get_latest_by = 'date'
