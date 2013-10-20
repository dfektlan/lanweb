from django.contrib import admin
from models import ItemGroup, Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('itemgroup','brand','product_model','holder')

admin.site.register(ItemGroup)
admin.site.register(Item, ItemAdmin)
