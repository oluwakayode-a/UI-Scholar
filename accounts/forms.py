from django.contrib.auth.forms import UserCreationForm
from django import forms
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
    