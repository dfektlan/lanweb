from django.contrib import admin
from models import Item, ItemGroup, ItemPack, Order, ItemQuantity


class ItemAdmin(admin.ModelAdmin):
    pass


class ItemGroupAdmin(admin.ModelAdmin):
    pass


class ItemPackAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class ItemQuantityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemGroup, ItemGroupAdmin)
admin.site.register(ItemPack, ItemPackAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ItemQuantity,ItemQuantityAdmin)


# Register your models here.
