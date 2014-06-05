# -*- coding: utf-8 -*-

import datetime

from django.db import models
from apps.userprofile.models import SiteUser
from django.utils import timezone


class RegisterToken(models.Model):
    user = models.ForeignKey(SiteUser)
    token = models.CharField("token", max_length=32)
    created = models.DateTimeField("created", editable=False, auto_now_add=True, default=datetime.datetime.now())

    @property
    def is_valid(self):
        valid_period = datetime.timedelta(days=1)
        now = timezone.make_aware(datetime.datetime.now(), timezone.get_default_timezone())
        return now < self.created + valid_period

