from django import template
from sponsor.models import Sponsor
from event.models import LanEvent


register = template.Library()

@register.inclusion_tag('sponsor/sponsor_list.html')

def show_sponsor_list():
    latest_event = LanEvent.objects.all().order_by('-start_date')[:1]
    sponsors = Sponsor.objects.filter(event=latest_event)

    return {'sponsors' : sponsors}
