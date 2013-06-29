from django.contrib import admin
from models import SiteUser

class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name')

admin.site.register(SiteUser, SiteUserAdmin)
