from django.conf.urls import patterns, include, url

urlpatterns = patterns('userprofile.views',
    url(r'^myprofile', 'myprofile', name='profile overview'),
)
