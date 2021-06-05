from django.urls import path

from . import views

app_name = 'changelog'

urlpatterns = [
    path('ragcp/', views.ragcp_changelog, name='ragcp_changelog'),
    path('rathena/', views.rathena_changelog, name='rathena_changelog'),
]
