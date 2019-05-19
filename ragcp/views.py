from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import *
from .models import *


def index(request):
    return render(request, 'index.html')


def forbidden(request):
    return render(request, '403.html')
