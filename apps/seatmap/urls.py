from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.seatmap.views',
    url(r'^edit/(?P<seatmap_id>\d+)/$', 'edit_seatmap', name='edit_seatmap'),
    url(r'^seats/(?P<seatmap_id>\d+)/$', 'seat_overview', name='seat_overview'),
    url(r'^save/$', 'save_seatmap', name='save_seatmap'),
)
