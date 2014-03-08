from django.db import models


class Channel(models.Model):
    channelName = models.CharField(max_length=40)
    displayName = models.CharField(max_length=60)

    def __unicode__(self):
        return self.displayName