from sponsor.models import Sponsor
from event.models import LanEvent
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    current_event = LanEvent.objects.get(current=True)
    sponsors = Sponsor.objects.filter(event=current_event)
    
    return render(request, 'sponsor/index.html', {'sponsors' : sponsors})
