from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Char


# Create your views here.
# view list of chars
@login_required
def char_list(request):
    if request.user.is_staff:
        chars = Char.objects.all()
    else:
        chars = Char.objects.filter(account_id=request.user.id)

    context = {
        'chars': chars,
        'char_count': len(chars)
    }
    return render(request, 'chars.html', context)

@login_required
def char_view(request, char_id):
    char = Char.objects.get(char_id=char_id)

    if char.account_id != request.user and not request.user.is_staff:
        return redirect('forbidden')

    context = {
        'char': char
    }
    return render(request, 'char_details.html', context)

@login_required
def char_reset_position(request, char_id):
    if request.POST:
        if 'reset-position' in request.POST:
            pass
        elif 'reset-map' in request.POST:
            return char_reset_map(request, char_id)
        elif 'reset-appearance' in request.POST:
            return char_reset_appearence(request, char_id)

        char = Char.objects.get(char_id=char_id)

        if char.account_id != request.user and not request.user.is_staff:
            return redirect('forbidden')

        char.reset_position()
        return redirect('char:char_view', char_id)
    else:
        return redirect('not_found')

@login_required
def char_reset_map(request, char_id):
    if request.POST:
        char = Char.objects.get(char_id=char_id)

        if char.account_id != request.user and not request.user.is_staff:
            return redirect('forbidden')

        char.reset_save_position()
        return redirect('char:char_view', char_id)
    else:
        return redirect('not_found')

@login_required
def char_reset_appearence(request, char_id):
    if request.POST:
        char = Char.objects.get(char_id=char_id)

        if char.account_id != request.user and not request.user.is_staff:
            return redirect('forbidden')

        char.reset_appearance()
        return redirect('char:char_view', char_id)
    else:
        return redirect('not_found')

