__author__ = 'kradalby'

from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.serializers import Serializer
from apps.userprofile.models import SiteUser


class UserResource(ModelResource):

    class Meta:
        queryset = SiteUser.objects.all()
        resource_name = 'crewmember'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json'])
        allowed_methods = ['get']
        excludes = ['nickname', 'date_of_birth', 'phone', 'skype',
                    'steam', 'address', 'town', 'zip_code', 'country',
                    'image', 'email', 'date_joined', 'is_true',
                    'is_staff', 'is_superuser', 'password']

