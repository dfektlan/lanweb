__author__ = 'kradalby'

from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.serializers import Serializer
from apps.event.models import LanEvent
from apps.userprofile.models import SiteUser


class UserResource(ModelResource):

    class Meta:
        queryset = SiteUser.objects.all()
        resource_name = 'crewmember'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json'])
        allowed_methods = ['get', 'patch']
