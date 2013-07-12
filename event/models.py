from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class LanEvent(models.Model):
    name = models.CharField(_(u'Navn'), max_length=200)
    description = models.TextField(_(u'Beskrivelse'), )
    start_date = models.DateTimeField(_(u'Start dato'), editable=True)
    end_date = models.DateTimeField(_(u'Slutt dato'), editable=True)

    def __unicode__(self):
        return self.name
