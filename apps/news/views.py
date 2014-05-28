# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from apps.news.models import Post
from apps.event.models import LanEvent
 
def overview(request, event=None):
# This view displays the posts related to the current event. It will display featured posts on top, else the latest post.
    print event

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
    
#    non_featured = Post.objects.filter(featured=False).filter(event=current_event)
#    posts = []
#    elements = []
#
#   Sends posts in parts of 3
#    for p in non_featured:
#        elements.append(p)
#        if len(elements) == 3:
#            posts.append(elements)
#            elements = []
#    posts.append(elements) 
    posts = Post.objects.filter(featured=False).filter(event=current_event)
    return render(request, 'news/overview.html', {'posts': posts, 'featured': featured, 'event': event})
 
def detail(request, news_id, event=None):
    post = get_object_or_404(Post, pk=news_id)
    return render(request, 'news/detail.html', {'post': post, 'event': event})

 
def archive(request, event=None, event_id=None):
#    event = get_object_or_404(LanEvent, pk=event_id)
#    filtered_posts = Post.objects.filter(event=event)
    events = LanEvent.objects.all()
    all_posts = Post.objects.all()
#   Sends posts in parts of 3
    posts = []
    elements = []
    for p in all_posts: # change to filtered_posts for URL-sorting
        elements.append(p)
        if len(elements) == 3:
            posts.append(elements)
            elements = []
    posts.append(elements) 
    print(posts)
    return render(request, 'news/archive.html', {'posts': posts, 'events': events, 'event': event})
    
