from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, editable=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)

#    published = models.BooleanField(default=True)
#    edited_by =
#    edited_date =

    class Meta:
        ordering = ['-created',]

    def __unicode__(self):
        return u'%s' % self.title

    def get_absolute_url(self):
        return reverse('news.views.detail', args=[self.slug])
