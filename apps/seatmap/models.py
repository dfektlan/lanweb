from django.db import models

from apps.event.models import LanEvent


class Seat(models.Model):

    STATUS = (
        (0, u'Ledig'),
        (1, u'Reservert'),
        (2, u'Lukket'),
    )

    status = models.SmallIntegerField(default=2, choices=STATUS)


class Row(models.Model):

    ORIENTATION = (
        (0, u'Vertikal'),
        (1, u'Horisontal')
    )

    row = models.IntegerField()
    orientation = models.SmallIntegerField(default=0, choices=ORIENTATION)
    position_x = models.IntegerField()
    position_y = models.IntegerField()


class Seatmap(models.Model):
    event = models.ForeignKey(LanEvent)
    width = models.IntegerField()
    height = models.IntegerField()
    rows = models.ManyToManyField(Row, blank=True)

    def __unicode__(self):
        return self.event.name


class RowSeat(models.Model):
    row = models.ForeignKey(Row, null=False)
    seat = models.ForeignKey(Seat, null=False)
    number = models.IntegerField()
