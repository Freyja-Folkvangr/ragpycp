from github import Github

from ragcp import settings


def get_simplified_commits(repository_name: str = None):
    g = Github(login_or_token=settings.GITHUB_TOKEN)
    repo = g.get_user().get_repo('ragpycp')
    for commit in repo.get_commits():
        if commit.author is not None:
            yield {
                'message': commit.commit.message,
                'avatar': commit.author.avatar_url,
                'username': commit.author.login,
                'date': commit.commit.last_modified,
                'url': commit.commit.url
            }
