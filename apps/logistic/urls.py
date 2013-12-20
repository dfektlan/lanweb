from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.logistic.views',
    url(r'^', 'index', name='logistic index'),
    
    )
