from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'users'

urlpatterns = [

    path('signup/', views.SignUp.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
