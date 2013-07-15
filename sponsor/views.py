from sponsor.models import Sponsor
from event.models import LanEvent
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    latest_event = LanEvent.objects.all().order_by('-start_date')[:1]
    sponsors = Sponsor.objects.filter(event=latest_event)
    
    return render(request, 'sponsor/index.html', {'sponsors' : sponsors})
