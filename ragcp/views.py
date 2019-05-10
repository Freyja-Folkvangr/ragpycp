from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import *
from .models import *


def index(request):
    return render(request, 'index.html')


def register(request):
    from django.core.validators import validate_email
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        userid = form.cleaned_data['userid']
        user_pass = form.cleaned_data['user_pass']
        validate_email(form.cleaned_data['email'])
        user.save()
        user = authenticate(username=userid, password=user_pass)
        if user is not None:
            if user.is_active:
                login(request, user)
                #albums = Album.objects.filter(user=request.user)
                albums = {}
                return render(request, 'index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #albums = Album.objects.filter(user=request.user)
                albums = {}
                return render(request, 'index.html', {'albums': albums})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)


def detail(request):
    pass


def delete_album(request):
    pass


def favorite_album(request):
    pass


def create_album(request):
    pass


def favorite(request):
    pass

def songs(request):
    pass
