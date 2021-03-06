from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    """
    Render (put together) our template blog/post_list.html
    Requires a request to run.
    """
    # posts is a Queryset of all Posts
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
