from django.urls import path
from . import views

app_name = 'thor'

urlpatterns = [

    path('config/<str:patcher_name>/', views.config, name='config'),
    path('config/<str:patcher_name>/patch_list/', views.patch_list, name='patch_list'),
]
