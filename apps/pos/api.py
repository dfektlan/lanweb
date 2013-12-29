from tastypie.resources import ModelResource
from tastypie import fields
from apps.pos.models import Item, ItemGroup, ItemPack, ItemQuantity, Order
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization


class ItemGroupResource(ModelResource):
    class Meta:
        queryset = ItemGroup.objects.all()
        resource_name = 'itemgroup'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class ItemResource(ModelResource):
    group = fields.ForeignKey(ItemGroupResource, 'group')

    class Meta:
        queryset = Item.objects.all()
        resource_name = 'item'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class ItemPackResource(ModelResource):
    group = fields.ForeignKey(ItemGroupResource, 'group')

    class Meta:
        queryset = ItemPack.objects.all()
        resource_name = 'itempack'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class ItemQuantityResource(ModelResource):
    order = fields.ForeignKey('apps.pos.api.OrderResource', 'order', related_name='itemquantity')
    item = fields.ForeignKey(ItemResource, 'item', full=True)

    class Meta:
        queryset = ItemQuantity.objects.all()
        resource_name = 'itemquantity'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class OrderResource(ModelResource):
    items = fields.ManyToManyField(ItemQuantityResource,
                                   attribute=lambda bundle: bundle.obj.item.through.objects.filter(
                                       order=bundle.obj) or bundle.obj.item, full=True)

    #workaround to allow ItemQuantityResource to point at OrderResource through a foreignkey
    itemquantity = fields.ForeignKey(ItemQuantityResource, 'itemquantity', null=True)

    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


