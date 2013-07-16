from django.shortcuts import render, get_object_or_404
from news.models import Post
 
def overview(request):
#check if there are featured posts, if not; get the latest post
    try:
        featured = Post.objects.filter(featured=True).latest()
    except Post.DoesNotExist:
#check if there are posts at all
        try:
            featured = Post.objects.latest()
        except Post.DoesNotExist:
            featured = None
    
    non_featured = Post.objects.filter(featured=False)
    posts = []
    elements = []

    for p in non_featured:
        elements.append(p)
        if len(elements) == 3:
            posts.append(elements)
            elements = []
    posts.append(elements)
    
    return render(request, 'news/overview.html', {'posts': posts, 'featured': featured})
 
def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'news/detail.html', {'post': post})
