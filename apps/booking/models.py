from django.db import models
from apps.event.models import LanEvent
from apps.userprofile.models import SiteUser


class Ticket(models.Model):

    MEMBER_TYPE = (
        (0, "Medlem"),
        (1, "Ikke medlem")
    )

    event = models.ForeignKey(LanEvent)
    name = models.CharField(max_length=30)
    available = models.BooleanField()
    visible = models.BooleanField()
    owner = models.ForeignKey(SiteUser)
    price_member = models.IntegerField()
    price_non_member = models.IntegerField()
    member_type = models.SmallIntegerField(choices=MEMBER_TYPE)


class Order(models.Model):
    owner = models.ForeignKey(SiteUser, editable=False)
    tickets = models.ManyToManyField(Ticket)
    stripe_id = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    paid = models.BooleanField()



