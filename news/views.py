from django.shortcuts import render, get_object_or_404
from news.models import Post
 
def overview(request):
# to get the posts that are published, use posts=Post.objects.filter(published=True)
    featured = Post.objects.filter(featured=True).latest()
    non_featured = Post.objects.filter(featured=False)
    posts = []
    elements = []
    counter = 0
    for p in non_featured:
        elements.append(p)
        if len(elements) == 3:
            posts.append(elements)
            elements = []
        counter += 1
    posts.append(elements)
    
    print(posts)
    return render(request, 'news/overview.html', {'posts': posts, 'featured': featured})
 
def detail(request, slug):
# get the Post object
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'news/detail.html', {'post': post})
