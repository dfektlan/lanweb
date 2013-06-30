from django.conf.urls import patterns, include, url

urlpatterns = patterns('crew.views',
    url(r'^application/overview', 'overview', name='application overview'),
    url(r'^application/look/(?P<application_id>\d+)/$', 'look', name='application look'),
    url(r'^application/user', 'user_overview', name='application user overview'),
)
