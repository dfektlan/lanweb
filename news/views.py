from django.shortcuts import render, get_object_or_404
from news.models import Post
 
def overview(request):
# to get the posts that are published, use posts=Post.objects.filter(published=True)
    posts = Post.objects.all
# now return the rendered template
    return render(request, 'news/overview.html', {'posts': posts})
 
def detail(request, slug):
# get the Post object
    post = get_object_or_404(Post, slug=slug)
# now return the rendered template
    return render(request, 'news/detail.html', {'post': post})
