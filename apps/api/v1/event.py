from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.serializers import Serializer
from apps.event.models import LanEvent


class LanEventResource(ModelResource):
    class Meta:
        queryset = LanEvent.objects.all()
        resource_name = 'lanevent'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        allowed_methods = ['get']

