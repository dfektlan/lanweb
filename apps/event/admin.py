from django.contrib import admin
from models import LanEvent

class LanEventAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'end_date',]

    def save_model(self, request, obj, form, change):
        if obj.current:
            lanevents = LanEvent.objects.all()
            for event in lanevents:
                if event.current:
                    event.current = False
                    event.save()
        obj.save()

admin.site.register(LanEvent, LanEventAdmin)
