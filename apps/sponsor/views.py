from apps.sponsor.models import Sponsor
from apps.event.models import LanEvent
from django.shortcuts import render, get_object_or_404, redirect

def index(request, event=None):
    eventObj = LanEvent.objects.get(shortname=event)
    sponsors = Sponsor.objects.filter(event=eventObj)
    
    return render(request, 'sponsor/index.html', {'sponsors' : sponsors, 'event': event})
