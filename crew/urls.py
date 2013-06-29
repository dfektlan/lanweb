from django.conf.urls import patterns, include, url

urlpatterns = patterns('crew.views',
    url(r'^applications', 'applications', name='applications'),
)
