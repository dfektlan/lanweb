# urls.py
from django.conf.urls import patterns, include, url
print("derp")

urlpatterns = patterns('',
    url(r'^', include('apps.api.v1.urls')),
)
