import feedparser
from django.shortcuts import render, redirect

# Create your views here.
from content.models import Post
from ragcp import settings
from ragcp.settings import logger
from users.models import Login


def get_feed(request):
    feed_url = settings.RSS_FEED

    if not feed_url or not settings.FEED_ENABLED or not request.user.is_staff:
        return redirect('forbidden')

    feed = feedparser.parse(feed_url)
    system_account = Login.objects.filter(sex='S').first()
    posts = Post.objects.filter(author__sex='S', parent=None).values_list('title', 'content', flat=True)
    logger.debug('Existing posts: %s' % posts)
    for post in feed['entries']:
        if (post.title, post.content) not in posts:
            p = Post(
                title=post.title,
                content=post.description,
                reference=post.link,
                author=system_account,
                parent=None
            ).save()
            logger.debug('post created: %s' % p)
    return redirect('index')
