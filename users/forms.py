from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Login


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Login
        fields = ('username', 'email', 'sex', 'birthdate')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Login
        fields = UserChangeForm.Meta.fields
