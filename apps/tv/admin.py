from django.contrib import admin
from apps.tv.models import Channel


class ChannelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Channel, ChannelAdmin)