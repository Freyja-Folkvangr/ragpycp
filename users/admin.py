# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Login


class MyUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        ('Ragnarok Settings', {'fields': ('state', 'sex', 'birthdate', 'character_slots')}),
        ('Ragnarok Privileges', {'fields': ('group_id', 'vip_time', 'old_group')}),
        ('Ragnarok Security',
         {'fields': ('pincode', 'pincode_change', 'unban_time', 'expiration_time', 'logincount', 'last_ip')})
    )
    list_display = ('username', 'id', 'email', 'is_staff', 'is_active', 'state')
    search_fields = ['id', 'username', 'email']
    list_filter = ['state', 'sex', 'is_active', 'is_staff', 'is_superuser']

admin.site.register(Login, MyUserAdmin)
