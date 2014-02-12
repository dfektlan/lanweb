from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.tv.views',
    url(r'^stream/(?P<stream_id>\d+)/$', 'stream', name='stream'),
)
