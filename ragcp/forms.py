from django import forms
from django.contrib.auth.models import User

from .models import *

class UserForm(forms.ModelForm):
    user_pass = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ['userid', 'sex', 'email', 'user_pass']
