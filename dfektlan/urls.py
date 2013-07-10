from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dfektlan.views.home', name='home'),
    # url(r'^dfektlan/', include('dfektlan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crew/',   include('crew.urls')),
    url(r'^logistic/',   include('logistic.urls')),
    url(r'^userprofile/',   include('userprofile.urls')),
    url(r'^news/', include('news.urls')),
     
)
