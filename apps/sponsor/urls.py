from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.sponsor.views',
    url(r'^', 'index', name='sponsor_index'),
)
