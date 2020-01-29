from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.shortcuts import Http404


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput())
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    password_confirm = forms.CharField(max_length=200, forms.PasswordInput())
    email = forms.EmailField()

    def clean(self):
        if username:
            if password != password_confirm:
                raise Http404