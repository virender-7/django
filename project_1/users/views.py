from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def user_register(request): 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')

    else:
        form = UserCreationForm()
    return render(request, "users/user_register.html", {'form':form})