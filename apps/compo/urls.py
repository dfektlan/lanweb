from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.compo.views',
    url(r'^$', 'overview', name='overview'),
)
