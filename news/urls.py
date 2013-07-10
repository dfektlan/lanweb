from django.conf.urls import patterns, include, url

urlpatterns = patterns('news.views',
    url(r'^overview', 'overview', name='news overview'),
    url(r'^(?P<slug>[\w\-]+)/$', 'detail', name='news detail'),
)
