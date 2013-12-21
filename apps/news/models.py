from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from apps.event.models import LanEvent

class Post(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, editable=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='news', blank=True, ) 
    event = models.ForeignKey(LanEvent, null=False, verbose_name="Event", related_name="Event_news", editable=True)

#    published = models.BooleanField(default=True)
#    edited_by =
#    edited_date =

    class Meta:
        ordering = ['-created',]
        get_latest_by = 'created'

    def __unicode__(self):
        return u'%s' % self.title
