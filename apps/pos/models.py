from django.db import models
from django.utils.translation import ugettext as _
from apps.event.models import LanEvent

class Order(models.Model):
    date = models.DateTimeField(_('Dato'), editable=False, auto_now_add=True)

class ItemGroup(models.Model):
    name = models.CharField(_('Navn'), max_length=200, blank=False, null=False)
    date = models.DateTimeField(_('Dato'), editable=False, auto_now_add=True)

class Item(models.Model):
    name = models.CharField(_('Navn'), max_length=200, blank=False, null=False)
    date = models.DateTimeField(_('Dato'), editable=False, auto_now_add=True)
    group = models.ForeignKey(ItemGroup, null=False, verbose_name="Item Group", editable=True)
    price = models.IntegerField(_('Pris'), blank=False)
    order = models.ForeignKey(Order, null=True, editable=False)

class ItemPack(models.Model):
    name = models.CharField(_('Navn'), max_length=200, blank=False, null=False)
    date = models.DateTimeField(_('Dato'), editable=False, auto_now_add=True)
    group = models.ForeignKey(ItemGroup, null=False, verbose_name="Item Group", editable=True)
    #many to many?


