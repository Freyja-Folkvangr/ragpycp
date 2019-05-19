from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'char'

urlpatterns = [

    path('list/', views.char, name='list'),
    path('<int:char_id>/', views.char_view, name='char_view'),
]
