from django.db import models
from django.utils.translation import ugettext as _

from apps.event.models import LanEvent

# Create your models here.

class Page(models.Model):
    
    url = models.CharField(_(u'URL'), max_length=20)
    title = models.CharField(_(u'Tittel'), max_length=20)
    content = models.TextField(_(u'Innhold'))
    events = models.ManyToManyField(LanEvent)

    def __unicode__(self):
        return self.title
