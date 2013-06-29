from django.contrib import admin
from models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user']
    def save_model(self, request, obj, form, change): 
        if not change:
            obj.user = request.user
        obj.save()

admin.site.register(Application, ApplicationAdmin)
