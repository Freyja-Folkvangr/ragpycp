from django.shortcuts import render, get_object_or_404

# Create your views here.
from thor.models import Patcher, CustomClient, Update


def config(request, patcher_name):
    patcher = get_object_or_404(Patcher, name=patcher_name)
    clients = CustomClient.objects.filter(patcher=patcher).order_by('created')

    # Set the custom client number
    i = 1
    for client in clients:
        client.i = i
        i += 1

    context = {
        'patcher': patcher,
        'clients': clients
    }
    return render(request, 'main_config.html', context)

def patch_list(request, patcher_name):
    patches = Update.objects.filter(patcher__name=patcher_name)

    context = {
        'patches': patches
    }
    return render(request, 'patch_list.html', context)
