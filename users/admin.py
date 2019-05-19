from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Login

class CustomUserAdmin(UserAdmin):
    model = Login
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(Login, CustomUserAdmin)