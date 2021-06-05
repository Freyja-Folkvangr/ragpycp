from django.urls import path

from . import views

app_name = 'servicedesk'

urlpatterns = [

    path('', views.tickets, name='tickets'),
    path('<int:ticket_id>/', views.ticket, name='ticket'),
    path('new/', views.new_ticket, name='new_ticket'),
]
