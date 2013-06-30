from django.conf.urls import patterns, include, url

urlpatterns = patterns('crew.views',
    url(r'^applications', 'applications_view', name='applications'),
)
