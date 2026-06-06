from django.shortcuts import render
from posts.models import Posts


# Create your views here.
def post_list(request):
    posts = Posts.objects.all().order_by('-date')
    return render(request, "posts/post_list.html", {'posts': posts})

def post_page(request, slug):
    post = Posts.objects.get(slug=slug)
    return render(request, "posts/post_page.html", {'post': post})
    
