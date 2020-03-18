from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import PermissionDenied, login_required
from django.shortcuts import redirect, render
from .forms import RegisterForm, ProfileForm, EditUserForm
from .models import Profile
from django.contrib import messages


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        
        return redirect('accounts:edit_profile')

    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def profile(request, id):
    user = Profile.objects.get(id=id)
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your Profile has been successfully updated.")
            return redirect(request.user.profile.get_absolute_url())
        else:
            messages.error(request, 'Please correct the errors')
    
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
    context = {
        'user_form' : user_form, 
        'profile_form' : profile_form
    }
    return render(request, 'accounts/edit_profile.html', context)



def log_out(request):
    logout(request)

    return redirect('/')
