from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.page.views',
    url(r'^(?P<url>.*)$', 'page', name='page'),
)
