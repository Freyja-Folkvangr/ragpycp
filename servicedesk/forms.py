from django import forms
from django.contrib.auth.models import User

from .models import *


class new_ticket_form(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['category', 'subject', 'body']

class new_ticket_reply(forms.ModelForm):
    class Meta:
        model = Replies
        fields = ['body', 'response_needed']