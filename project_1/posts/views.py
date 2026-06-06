from django.shortcuts import render, redirect
from posts.models import Posts
from django.contrib.auth.decorators import login_required
from posts import forms

# Create your views here.
def post_list(request):
    posts = Posts.objects.all().order_by('-date')
    return render(request, "posts/post_list.html", {'posts': posts})

def post_page(request, slug):
    post = Posts.objects.get(slug=slug)
    return render(request, "posts/post_page.html", {'post': post})
 
@login_required(login_url="/users/login")
def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
           #Save with User
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts:list')


    else:    
        form = forms.CreatePost()
    return render(request, "posts/post_new.html", {'form':form})

    
    
