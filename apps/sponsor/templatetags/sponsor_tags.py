from django import template
from sponsor.models import Sponsor
from event.models import LanEvent


register = template.Library()

@register.inclusion_tag('sponsor/sponsor_list.html')

def show_sponsor_list():
    current_event = LanEvent.objects.get(current=True)
    sponsors = Sponsor.objects.filter(event=current_event)

    return {'sponsors' : sponsors}
