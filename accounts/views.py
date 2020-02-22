from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/')
    
    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)

def log_out(request):
    logout(request)
    
    return redirect('/')
