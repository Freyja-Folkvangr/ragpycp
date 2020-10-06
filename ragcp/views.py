from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from content.models import Post
from .forms import *
from .models import *


def index(request):
    context = {}
    try:
        context['posts'] = Post.objects.filter(parent=None).order_by('-added')[:15]
    except Exception as e:
        context['posts'] = None
    return render(request, 'index.html', context)


def forbidden(request):
    return render(request, '403.html')
