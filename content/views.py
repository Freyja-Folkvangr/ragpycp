import feedparser
from django.shortcuts import render, redirect

# Create your views here.
from content.forms import new_entry_form
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
    posts = Post.objects.filter(author__sex='S', parent=None).values_list('title', 'content')
    logger.debug('Existing posts: %s' % posts)
    for post in feed['entries']:
        post.description = post.description.replace('\n', '<br>')
        if (post.title, post.description) not in posts:
            p = Post(
                title=post.title,
                content=post.description,
                reference=post.link,
                author=system_account,
                parent=None
            ).save()
            logger.debug('post created: %s' % p)
    return redirect('index')

def new_entry(request):
    if not request.user.is_staff:
        redirect('forbidden')

    form = new_entry_form(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.content = post.content.replace('\n', '<br>')
        form.save()
        return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'new_entry.html', context)
