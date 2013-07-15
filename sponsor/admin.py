from django.contrib import admin
from models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'event', 'logo', 'url',]

admin.site.register(Sponsor, SponsorAdmin)
