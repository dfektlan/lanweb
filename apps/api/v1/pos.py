from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.serializers import Serializer
from apps.pos.models import Item, ItemGroup, ItemPack, ItemQuantity, Order
from apps.event.models import LanEvent


class ItemGroupResource(ModelResource):
    class Meta:
        queryset = ItemGroup.objects.all()
        resource_name = 'itemgroup'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        allowed_methods = ['get']


class ItemResource(ModelResource):
    group = fields.ForeignKey(ItemGroupResource, 'group')

    class Meta:
        queryset = Item.objects.all()
        resource_name = 'item'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        allowed_methods = ['get']



class ItemPackResource(ModelResource):
    group = fields.ForeignKey(ItemGroupResource, 'group')

    class Meta:
        queryset = ItemPack.objects.all()
        resource_name = 'itempack'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json', 'jsonp'])



class ItemQuantityResource(ModelResource):
    order = fields.ForeignKey('apps.api.v1.pos.OrderResource', 'order', related_name='itemquantity')
    item = fields.ForeignKey(ItemResource, 'item', full=True)

    class Meta:
        queryset = ItemQuantity.objects.all()
        resource_name = 'itemquantity'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json', 'jsonp'])



class OrderResource(ModelResource):
    items = fields.ManyToManyField(ItemQuantityResource,
                                   attribute=lambda bundle: bundle.obj.item.through.objects.filter(
                                       order=bundle.obj) or bundle.obj.item, full=True, null=True, readonly=True)

    #workaround to allow ItemQuantityResource to point at OrderResource through a foreignkey
    itemquantity = fields.ForeignKey(ItemQuantityResource, 'itemquantity', null=True)

    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        serializer = Serializer(formats=['json', 'jsonp'])
        always_return_data = True

    def hydrate(self, bundle):
        bundle.obj.event = LanEvent.objects.filter(current=True)[0]
        #bundle.data['event'] = LanEvent.objects.filter(current=True)[0]
        return bundle




