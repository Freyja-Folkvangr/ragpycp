from django.db.models import Q
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.utils import timezone

from thor.models import CustomClient, Patcher, Update


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
    """

    :param request: django request
    :param patcher_name: str name of the Patcher object

    This function will query updates in order to render the patch list that is being read by Thor Patcher.
    The available_since value must be None:now or greater or equal than now in current timezone

    :return: render patch list
    """
    now = timezone.now()

    query = Q(patcher__name=patcher_name)
    query &= (Q(available_since=None) | Q(available_since__gte=now))

    patches = Update.objects.filter(query)

    context = {
        'patches': patches
    }
    return render(request, 'patch_list.html', context)
