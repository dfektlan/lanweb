from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.userprofile.views',
    url(r'^myprofile', 'myprofile', name='myprofile'),
    url(r'^profile/(?P<user_id>\d+)/$', 'profile', name='profile'),
)
