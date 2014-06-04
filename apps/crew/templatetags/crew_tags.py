from django import template
from apps.crew.models import CrewMember
from apps.event.models import LanEvent

register = template.Library()

@register.assignment_tag()
def getCrewMemberData(user, event):
    eventObj = LanEvent.objects.filter(shortname=event)
    crewMemberData = CrewMember.objects.filter(user=user, event=eventObj)
    if len(crewMemberData) == 1:
        print crewMemberData[0]
        return crewMemberData[0]
    else:
        return None

