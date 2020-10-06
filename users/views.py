from django.shortcuts import render

# Create your views here.
# users/views.py
from django.urls import reverse_lazy
from django.views import generic
import random

from .forms import CustomUserCreationForm
from .models import Login


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    def form_valid(self, form):
        user = form.save(commit=False)

        tokens = Login.objects.all().values_list('web_auth_token', flat=True)
        token = None
        while token in tokens or token == None:
            token = str(random.randrange(1000000000))

        user.web_auth_token = token
        return super().form_valid(form)