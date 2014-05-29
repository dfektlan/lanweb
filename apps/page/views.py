from django.shortcuts import render
from django.http import Http404


from apps.page.models import Page
from apps.event.models import LanEvent
# Create your views here.

def page(request, event=None, url=None):
    p = Page.objects.get(url=url)
    events = p.events.all()
    eventObj = LanEvent.objects.get(shortname=event)

    if eventObj not in events:
        raise Http404

    return render(request, 'page/page.html', {'page': p, 'event': event})
