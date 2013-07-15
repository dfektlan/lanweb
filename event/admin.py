from django.contrib import admin
from models import LanEvent

class LanEventAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'end_date',]

admin.site.register(LanEvent, LanEventAdmin)
