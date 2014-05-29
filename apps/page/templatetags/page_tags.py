from django import template
from apps.event.models import LanEvent
from apps.page.models import Page


register = template.Library()


@register.assignment_tag(takes_context=True)
def get_pages(context, event, url):
    eventObj = LanEvent.objects.get(shortname=event)
    pages = Page.objects.filter(events=eventObj).filter(url__startswith=url)

    return pages

