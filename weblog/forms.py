from django import forms
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ('username','password',)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"