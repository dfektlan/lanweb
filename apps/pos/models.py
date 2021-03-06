from django.db import models
from django.utils.translation import ugettext as _
from apps.event.models import LanEvent


class ItemGroup(models.Model):
    name = models.CharField(_('Navn'), max_length=200, blank=False, null=False)
    date = models.DateTimeField(_('Dato'), editable=False, auto_now_add=True)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(_('Navn'), max_length=200, blank=False, null=False)
    date = models.DateTimeField(_('Dato'), editable=False, auto_now_add=True)
    group = models.ForeignKey(ItemGroup, null=False, verbose_name="Item Group", editable=True)
    price = models.IntegerField(_('Pris'), blank=False)

    def __unicode__(self):
        return self.name


class Order(models.Model):
    date = models.DateTimeField(_('Dato'), editable=False, auto_now_add=True)
    items = models.ManyToManyField(Item, null=True, editable=True, through='ItemQuantity')
    event = models.ForeignKey(LanEvent, null=False)
    paymentMethod = models.CharField(_('Betalingsmetode'), max_length=10, null=False)

    def __unicode__(self):
        return "Order " + str(self.pk)


class ItemPack(models.Model):
    name = models.CharField(_('Navn'), max_length=200, blank=False, null=False)
    date = models.DateTimeField(_('Dato'), editable=False, auto_now_add=True)
    group = models.ForeignKey(ItemGroup, null=False, verbose_name="Item Group", editable=True)
    items = models.ManyToManyField(Item)
    
    def __unicode__(self):
        return self.name


class ItemQuantity(models.Model):
    order = models.ForeignKey(Order, null=False)
    item = models.ForeignKey(Item, null=False)
    quantity = models.IntegerField()
    totalPrice = models.IntegerField()

    def __unicode__(self):
        return "Item Quantity " + str(self.pk)
