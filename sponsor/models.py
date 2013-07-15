from django.db import models
from event.models import LanEvent
from django.utils.translation import ugettext as _

class Sponsor(models.Model):
    latest_event = LanEvent.objects.all().order_by('-start_date')[:1]

    name = models.CharField(_(u'Navn'), max_length=200)
    description = models.TextField(_(u'Beskrivelse'), )
    event = models.ForeignKey(LanEvent, null=False, default=latest_event, verbose_name="Event", related_name="Event", editable=True)
    logo = models.ImageField(_(u'Logo'), upload_to='sponsor', max_length=150, blank=False)
    url = models.URLField(_(u'URL'), max_length=200, blank=True)
    
    def __unicode__(self):
        return (self.name)
