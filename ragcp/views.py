from django.shortcuts import render
from content.models import Post


def index(request):
    context = {}
    try:
        context['posts'] = Post.objects.filter(parent=None, deleted=False).order_by('-added')[:15]
    except Exception as e:
        context['posts'] = None
    return render(request, 'index.html', context)


def forbidden(request):
    return render(request, '403.html')
