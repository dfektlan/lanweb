from django.contrib import admin
from models import Application, Crew, CrewGroup, CrewShift

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user']
    def save_model(self, request, obj, form, change): 
        if not change:
            obj.user = request.user
        obj.save()

class CrewAdmin(admin.ModelAdmin):
    list_display = ['name']

class CrewGroupAdmin(admin.ModelAdmin):
    list_display = ['name','crew','event']

    def save_model(self, request, obj, form, change):
        obj.save()
        if not change:
            crewshift = CrewShift(crewgroup=obj, name="Flexi", description="Flexi")
            crewshift.save()

class CrewShiftAdmin(admin.ModelAdmin):
    list_display = ['name','crewgroup']

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Crew, CrewAdmin)
admin.site.register(CrewGroup, CrewGroupAdmin)
admin.site.register(CrewShift, CrewShiftAdmin)
