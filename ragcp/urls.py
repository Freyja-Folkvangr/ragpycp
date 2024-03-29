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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from ragcp.views import forbidden, index, trigger_error

app_name = 'ragcp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),

    url(r'^$', index, name='index'),

    url('403/', forbidden, name='forbidden'),

    path('users/', include('users.urls')),  # new
    path('users/', include('django.contrib.auth.urls')),  # new
    path('accounts/', include('django.contrib.auth.urls')),  # new

    path('char/', include('char.urls')),
    path('servicedesk/', include('servicedesk.urls')),
    path('content/', include('content.urls')),
    path('thor/', include('thor.urls')),
    path('changelog/', include('changelog.urls')),

]
