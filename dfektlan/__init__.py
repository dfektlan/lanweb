# -*- coding: utf-8 -*-

# Auto-create ApiKey objects after User is saved.
from django.db import models
from tastypie.models import create_api_key
from apps.userprofile.models import SiteUser as User
models.signals.post_save.connect(create_api_key, sender=User)
