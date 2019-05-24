from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'char'

urlpatterns = [

    path('list/', views.char, name='list'),
    path('<int:char_id>/', views.char_view, name='char_view'),
    path('<int:char_id>/reset_appearence/', views.char_reset_appearence, name='char_reset_appearence'),
    path('<int:char_id>/reset_map/', views.char_reset_map, name='char_reset_map'),
    path('<int:char_id>/reset_position/', views.char_reset_position, name='char_reset_position'),
]
