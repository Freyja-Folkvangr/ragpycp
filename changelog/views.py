from django.http import HttpResponseServerError
from django.shortcuts import redirect, render

# Create your views here.
from changelog.utils import get_simplified_commits
from ragcp import settings


def ragcp_changelog(request):
    if not settings.CHANGELOG_ENABLED or not settings.RAGCP_CHANGELOG:
        return redirect('index')
    elif not settings.GITHUB_TOKEN:
        return HttpResponseServerError('Github token is missing')

    context = {
        'commits': get_simplified_commits(settings.RAGCP_REPO_NAME)
    }

    return render(request, 'ragcp_changelog.html', context)

def rathena_changelog(request):
    if not settings.CHANGELOG_ENABLED or not settings.RATHENA_CHANGELOG:
        return redirect('index')
    elif not settings.GITHUB_TOKEN:
        return HttpResponseServerError('Github token is missing')

    context = {
        'commits': get_simplified_commits(settings.RATHENA_REPO_NAME)
    }

    return render(request, 'rathena_changelog.html', context)
