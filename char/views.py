from django.shortcuts import render, redirect
from .models import Char


# Create your views here.
# view list of chars
def char(request):
    if request.user.is_staff:
        chars = Char.objects.all()
    else:
        chars = Char.objects.filter(account_id=request.user.id)

    context = {
        'chars': chars,
        'char_count': len(chars)
    }
    return render(request, 'chars.html', context)


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


def char_reset_map(request, char_id):
    if request.POST:
        char = Char.objects.get(char_id=char_id)

        if char.account_id != request.user and not request.user.is_staff:
            return redirect('forbidden')

        char.reset_save_position()
        return redirect('char:char_view', char_id)
    else:
        return redirect('not_found')


def char_reset_appearence(request, char_id):
    if request.POST:
        char = Char.objects.get(char_id=char_id)

        if char.account_id != request.user and not request.user.is_staff:
            return redirect('forbidden')

        char.reset_appearance()
        return redirect('char:char_view', char_id)
    else:
        return redirect('not_found')

# view a single char
def char_view(request, char_id):
    char = Char.objects.get(char_id=char_id)

    if char.account_id != request.user and not request.user.is_staff:
        return redirect('forbidden')

    context = {
        'char': char
    }
    return render(request, 'char.html', context)
