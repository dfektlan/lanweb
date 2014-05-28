from apps.sponsor.models import Sponsor
from apps.event.models import LanEvent
from django.shortcuts import render, get_object_or_404, redirect

def index(request, event=None):
    current_event = LanEvent.objects.get(current=True)
    sponsors = Sponsor.objects.filter(event=current_event)
    
    return render(request, 'sponsor/index.html', {'sponsors' : sponsors})
