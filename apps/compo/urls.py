from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.compo.views',
    url(r'^$', 'overview', name='tournament_overview'),
    url(r'^tournament/(?P<tournament_id>\d+)/$', 'tournament', name='tournament'),
    url(r'^tournament/join/(?P<tournament_id>\d+)/$', 'register_to_tournament', name='register_to_tournament'),
    url(r'^tournament/check/(?P<tournament_id>\d+)/$', 'check_user', name='check_user'),
    url(r'^tournament/remove/(?P<tournament_id>\d+)/$', 'remove_participant', name='remove_participant'),
    url(r'^tournament/(?P<tournament_id>\d+)/create_tournament/$', 'create_tournament', name='create_tournament'),
    url(r'^tournament/start/(?P<tournament_id>\d+)/$', 'start_tournament', name='start_tournament'),
    url(r'^tournament/destroy/(?P<tournament_id>\d+)/$', 'destroy_tournament', name='destroy_tournament'),
    url(r'^tournament/finalize/(?P<tournament_id>\d+)/$', 'finalize_tournament', name='finalize_tournament'),
    url(r'^tournament/(?P<tournament_id>\d+)/add_team/$', 'add_team', name='add_team'),

)
