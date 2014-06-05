from django import template
from apps.event.models import LanEvent


register = template.Library()

@register.inclusion_tag('eventinfo.html')
#@register.assignment_tag(takes_context=True)

def get_latest_lanevent(event):
    eventObj = LanEvent.objects.get(shortname=event)
    return {'lanevent' : eventObj}
