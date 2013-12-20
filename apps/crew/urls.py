from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.crew.views',
    url(r'^application/overview', 'overview', name='overview'),
    url(r'^application/look/(?P<application_id>\d+)/$', 'look', name='look'),
    url(r'^application/user', 'user_overview', name='user_overview'),
    url(r'^application/new', 'new_application', name='new_application'),
    url(r'^application/edit/(?P<application_id>\d+)/$', 'new_application', name='edit_application'),
)
