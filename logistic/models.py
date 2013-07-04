from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import ugettext as _

class ItemGroup(models.Model):
    name = models.CharField(_("Navn"), max_length=200)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    itemgroup = models.ForeignKey(ItemGroup)
    brand = models.CharField(_("Merke"), max_length=200)
    product_model = models.CharField(_("Produkt modell"), max_length=200)
    description = models.CharField(_("Beskrivelse"), max_length=30)
    holder = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None, verbose_name="Current holder", related_name ="Holder", editable=True)

    def __unicode__(self):
        return self.product_model
