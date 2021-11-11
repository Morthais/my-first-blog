from django.shortcuts import render

def post_list(request):
    """
    Render (put together) our template blog/post_list.html
    Requires a request.
    """
    return render(request, 'blog/post_list.html', {})
