from django import template
from apps.sponsor.models import Sponsor
from apps.event.models import LanEvent


register = template.Library()

@register.inclusion_tag('sponsor/sponsor_list.html')

def show_sponsor_list(event):
    eventObj = LanEvent.objects.get(shortname=event)
    sponsors = Sponsor.objects.filter(event=eventObj)

    return {'sponsors' : sponsors}
