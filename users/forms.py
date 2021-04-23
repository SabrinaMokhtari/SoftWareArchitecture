from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    mobile = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile']

