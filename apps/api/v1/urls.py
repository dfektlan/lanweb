# urls.py
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from apps.api.v1.pos import ItemResource, ItemGroupResource, ItemPackResource, OrderResource, ItemQuantityResource

v1_api = Api(api_name='v1')
v1_api.register(ItemResource())
v1_api.register(ItemGroupResource())
v1_api.register(ItemPackResource())
v1_api.register(OrderResource())
v1_api.register(ItemQuantityResource())


urlpatterns = patterns('',
    url(r'^', include(v1_api.urls)),
)
