from django.db import models
from django.conf import settings

class Application(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, editable=False)
    about = models.TextField()
    why = models.TextField()
    licens = models.CharField(max_length=200)


