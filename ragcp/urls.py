"""ragcp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ragcp.views import index
from django.conf.urls import url
from . import views

app_name = 'ragcp'

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^$', index, name='index'),

    url(r'^login_user/', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/', views.register, name='register'),

    url(r'^detail/', views.detail, name='detail'),
    url(r'^delete_album/', views.delete_album, name='delete_album'),
    url(r'^favorite_album/', views.favorite_album, name='favorite_album'),
    url(r'^create_album/', views.create_album, name='create_album'),
    url(r'^favorite/', views.favorite, name='favorite'),
    url(r'^songs/', views.songs, name='songs'),

]
