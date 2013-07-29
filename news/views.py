# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from news.models import Post
from event.models import LanEvent

def overview(request):
# This view displays the posts related to the current event. It will display featured posts on top, else the latest post.

    current_event = LanEvent.objects.get(current=True)
#check if there are featured posts (to current event), if not; get the latest post
    try:
        featured = Post.objects.filter(event=current_event).filter(featured=True).latest()
    except Post.DoesNotExist:
#check if there are posts at all (to current event)
        try:
            featured = Post.objects.filter(event=current_event).latest()
        except Post.DoesNotExist:
            featured = None
    
    non_featured = Post.objects.filter(featured=False).filter(event=current_event)
    posts = []
    elements = []

    for p in non_featured:
        elements.append(p)
        if len(elements) == 3:
            posts.append(elements)
            elements = []
    posts.append(elements)
    print(featured) 
    return render(request, 'news/overview.html', {'posts': posts, 'featured': featured})
 
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'news/detail.html', {'post': post})

# følgende view er IKKE ferdig 
def archive(request, event_id=None):
    event = get_object_or_404(Event, pk=event_id)
    posts = Post.objects.filter(event=event)
    return render(request, 'news/archive.html', {'posts': posts})
    
