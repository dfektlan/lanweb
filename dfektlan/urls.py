from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'apps.news.views.overview', name='root'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),    
    # url(r'^dfektlan/', include('dfektlan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crew/',   include('apps.crew.urls')),
    url(r'^logistic/',   include('apps.logistic.urls')),
    url(r'^userprofile/',   include('apps.userprofile.urls')),
    url(r'^news/',  include('apps.news.urls')),
    url(r'^sponsor/',  include('apps.sponsor.urls')),
    url(r'^auth/',  include('apps.authentication.urls')),
    url(r'^pos/',  include('apps.pos.urls')),
)
#Fix for flatpages urls
urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
    )

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
        (r'^500/$', 'django.views.defaults.server_error'),
    )
