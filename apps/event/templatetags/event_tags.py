from django import template
from apps.event.models import LanEvent


register = template.Library()


@register.inclusion_tag('eventinfo.html')
def getEventInformation(event):
    eventObj = LanEvent.objects.get(shortname=event)
    return {'lanevent' : eventObj}



# This will set the event if it is not set, this is a hack so 404 pages dont give stacktraces. lol
@register.assignment_tag(takes_context=True)
def setEventIfNone(context, event):
    print event
    if event == "":
        event = "s14"
    print event
    print "IDENTIFY ME"
    return event

