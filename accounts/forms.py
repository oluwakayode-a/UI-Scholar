from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.shortcuts import Http404
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'profile_pic',
            'desc',
            'bio',
        ]