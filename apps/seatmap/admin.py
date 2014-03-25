from django.contrib import admin

from apps.seatmap.models import Seatmap, Row, Seat


class SeatmapAdmin(admin.ModelAdmin):
    pass

class RowAdmin(admin.ModelAdmin):
    pass

class SeatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Seatmap, SeatmapAdmin)
admin.site.register(Row, RowAdmin)
admin.site.register(Seat, SeatAdmin)
