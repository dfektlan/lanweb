from django.db import models

from apps.event.models import LanEvent


class Seat(models.Model):

    STATUS = (
        (0, u'Ledig'),
        (1, u'Reservert'),
        (2, u'Lukket'),
    )

    row = models.ForeignKey("Row")
    status = models.SmallIntegerField(default=2, choices=STATUS)
    number = models.IntegerField()

    def __unicode__(self):
        return self.row.seatmap.event.name + " - Row: " + str(self.row.row) + " Seat: " + str(self.number)

    class Meta:
        index_together = [
            ["row", "number"],
        ]
        unique_together = ("row", "number")


class Row(models.Model):

    ORIENTATION = (
        (0, u'Vertikal'),
        (1, u'Horisontal')
    )

    seatmap = models.ForeignKey("Seatmap")
    row = models.IntegerField()
    orientation = models.SmallIntegerField(default=0, choices=ORIENTATION)
    position_x = models.IntegerField()
    position_y = models.IntegerField()

    def __unicode__(self):
        return self.seatmap.event.name + " - Row: " + str(self.row)

    class Meta:
        index_together = [
            ["seatmap", "row"],
        ]
        unique_together = ("seatmap", "row")


class Seatmap(models.Model):
    event = models.ForeignKey(LanEvent)
    width = models.IntegerField()
    height = models.IntegerField()
    #rows = models.ManyToManyField(Row, blank=True)

    def __unicode__(self):
        return self.event.name
