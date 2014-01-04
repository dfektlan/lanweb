__author__ = 'kradalby'

from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.serializers import Serializer
from apps.event.models import LanEvent
from apps.crew.models import CrewMember
from apps.api.v1.userprofile import UserResource

class CrewMemberResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = CrewMember.objects.all()
        resource_name = 'crewmember'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json'])
        allowed_methods = ['get', 'patch']
