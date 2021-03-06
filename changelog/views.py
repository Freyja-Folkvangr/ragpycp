from django.http import HttpResponseServerError
from django.shortcuts import render, redirect

# Create your views here.
from github import Github

from ragcp import settings


def ragcp_changelog(request):
    if not settings.CHANGELOG_ENABLED or not settings.RAGCP_CHANGELOG:
        return redirect('index')
    elif not settings.GITHUB_TOKEN:
        return HttpResponseServerError('Github token is missing')

    g = Github(login_or_token=settings.GITHUB_TOKEN)
    repo = g.get_user().get_repo('ragpycp')
    commits = []
    for commit in repo.get_commits():
        if commit.author is not None:
            commits.append(
                {
                    'message': commit.commit.message,
                    'avatar': commit.author.avatar_url,
                    'username': commit.author.login,
                    'date': commit.commit.last_modified,
                    'url': commit.commit.url
                }
            )

    context = {
        'repo': repo,
        'commits': commits
    }

    return render(request, 'ragcp_changelog.html', context)
