from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView



# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
from django.contrib import admin
admin.autodiscover()

# dfekt LAN
dpatterns = [
    url(r'^$', 'apps.news.views.overview', name='root'),
    url(r'^auth/',  include('apps.authentication.urls')),
    url(r'^userprofile/',   include('apps.userprofile.urls')),
    url(r'^logistic/',    include('apps.logi.urls')),
    url(r'^crew/',   include('apps.crew.urls')),
    url(r'^news/',  include('apps.news.urls')),
    url(r'^sponsor/',  include('apps.sponsor.urls')),
    url(r'^pos/',  include('apps.pos.urls')),
    url(r'^compo/',  include('apps.compo.urls')),
    url(r'^tv/',  include('apps.tv.urls')),
]

eventpatterns = [
    url(r'^(?P<event>(s14))/', include(dpatterns)),
    url(r'^(?P<event>(v14))/', include(dpatterns)),

]

urlpatterns = patterns('',
    # Django
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages(?P<url>.*)$', 'django.contrib.flatpages.views.flatpage', name='flatpage'),

    # Update this to latest event!
    url(r'^$', RedirectView.as_view(url='s14/')),
    url(r'^api/',    include('apps.api.urls')),
)

urlpatterns += eventpatterns

#Fix for flatpages urls
#urlpatterns += patterns('django.contrib.flatpages.views',
#    (r'^(?P<url>.*/)$', 'flatpage'),
#    )

 

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
        (r'^500/$', 'django.views.defaults.server_error'),
    )
