from django.contrib import admin

# Register your models here.
from thor.models import Patcher, CustomClient, Update

class PatcherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'allow', 'force_start', 'policy_msg']
    list_filter = ['allow', 'force_start']
    search_fields = ['name', 'policy_msg']
    list_display_links = ['name']
    ordering = ['id']

class CustomClientAdmin(admin.ModelAdmin):
    list_display = ['patcher', 'name', 'checksum', 'path']
    search_fields = ['name', 'path']
    list_filter = ['patcher']
    list_display_links = ['name']

class UpdateAdmin(admin.ModelAdmin):
    list_display = ['id', 'filename', 'patcher']
    list_filter = ['patcher']
    search_fields = ['filename']
    list_display_links = ['filename']
    ordering = ['-id', '-created']

admin.site.register(Patcher, PatcherAdmin)
admin.site.register(CustomClient, CustomClientAdmin)
admin.site.register(Update, UpdateAdmin)