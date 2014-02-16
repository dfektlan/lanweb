from django.contrib import admin
from models import Game,Tournament,Participant,Team


class GameAdmin(admin.ModelAdmin):
    pass


class TournamentAdmin(admin.ModelAdmin):
    exclude = ['status', 'open', 'max_participants']


class ParticipantAdmin(admin.ModelAdmin):
    pass


class TeamAdmin(admin.ModelAdmin):
    pass


admin.site.register(Game,GameAdmin)
admin.site.register(Tournament,TournamentAdmin)
admin.site.register(Participant,ParticipantAdmin)
admin.site.register(Team,TeamAdmin)
