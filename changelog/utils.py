from datetime import timedelta

from django.utils import timezone
from github import Github

from ragcp import settings


def get_simplified_commits(repository_name: str = None):
    if not repository_name:
        yield

    g = Github(login_or_token=settings.GITHUB_TOKEN)
    repo = g.get_user().get_repo(repository_name)

    last_six_months = timezone.now() - timedelta(days=30*6)
    for commit in repo.get_commits(since=last_six_months):
        if commit.author is not None:
            yield {
                'message': commit.commit.message,
                'avatar': commit.author.avatar_url,
                'username': commit.author.login,
                'date': commit.commit.last_modified,
                'url': commit.commit.url
            }
