from django.conf.urls import patterns, include, url

urlpatterns = patterns('sponsor.views',
    url(r'^', 'index', name='sponsor_index'),
)
