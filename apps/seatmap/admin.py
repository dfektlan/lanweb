from django.contrib import admin

from apps.seatmap.models import Seatmap, Row, Seat


class SeatmapAdmin(admin.ModelAdmin):
    pass


admin.site.register(Seatmap, SeatmapAdmin)
