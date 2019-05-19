from django.shortcuts import render, redirect
from .models import Char


# Create your views here.
def char(request):
    chars = Char.objects.filter(account_id=request.user.id)

    context = {
        'chars': chars,
        'char_count': len(chars)
    }
    print(context)
    return render(request, 'char.html', context)


def char_view(request, char_id):
    char = Char.objects.get(char_id=char_id)

    if char.account_id.id != request.user.id:
        return redirect('forbidden')

    context = {
        'char': char
    }
    return render(request, 'char_view.html', context)
