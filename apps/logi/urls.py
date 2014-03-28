from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.logi.views',
    url(r'^overview', 'item_overview', name='item_overview'),
    url(r'^item/new', 'new_item', name='new_item'),
    url(r'^item/ edit/(?P<item_id>\d+)/$', 'new_item', name='edit_item'),

)
