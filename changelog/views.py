from django.http import HttpResponseServerError
from django.shortcuts import render, redirect

# Create your views here.
from changelog.utils import get_simplified_commits
from ragcp import settings


def ragcp_changelog(request):
    if not settings.CHANGELOG_ENABLED or not settings.RAGCP_CHANGELOG:
        return redirect('index')
    elif not settings.GITHUB_TOKEN:
        return HttpResponseServerError('Github token is missing')

    context = {
        'commits': get_simplified_commits('ragpycp')
    }

    return render(request, 'ragcp_changelog.html', context)
