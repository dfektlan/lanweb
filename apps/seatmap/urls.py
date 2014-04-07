from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.seatmap.views',
    url(r'^admin/edit/(?P<seatmap_id>\d+)/$', 'edit_seatmap', name='edit_seatmap'),
    url(r'^admin/seats/(?P<seatmap_id>\d+)/$', 'seat_overview', name='seat_overview'),
    url(r'^participant/(?P<seatmap_id>\d+)/$', 'participant_seatmap', name='participant_seatmap'),
    url(r'^admin/save/$', 'save_seatmap', name='save_seatmap'),
)
