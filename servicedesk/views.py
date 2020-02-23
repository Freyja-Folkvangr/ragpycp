from django.shortcuts import render, redirect
from servicedesk.models import Ticket, Replies
from .forms import new_ticket_form, new_ticket_reply

# Create your views here.

def tickets(request):
    if request.user.is_staff:
        tickets = Ticket.objects.all().order_by('state', 'created')
    else:
        tickets = Ticket.objects.filter(created_by=request.user.id).order_by('state', 'created')

    context = {
        'tickets': tickets,
        'ticket_count': len(tickets)
    }
    return render(request, 'tickets.html', context)

def ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    responses = Replies.objects.filter(ticket=ticket).order_by('created')

    if ticket.created_by != request.user and not request.user.is_staff:
        return redirect('forbidden')

    form = new_ticket_reply(request.POST or None)

    if form.is_valid():
        response = form.save(commit=False)
        response.created_by = request.user
        response.ticket = ticket
        response.save()
        return redirect('servicedesk:tickets')

    context = {
        'ticket': ticket,
        'responses': responses,
        'form': form
    }
    return render(request, 'ticket.html', context)

def new_ticket(request):
    form = new_ticket_form(request.POST or None)

    if form.is_valid():
        ticket = form.save(commit=False)
        ticket.created_by = request.user
        ticket.save()
        return redirect('servicedesk:tickets')

    context = {
        'form': form
    }

    return render(request, 'new_ticket.html', context)
