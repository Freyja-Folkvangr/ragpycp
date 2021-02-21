import feedparser
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from content.forms import new_entry_form, write_response_form
from content.models import Post
from ragcp import settings
from ragcp.settings import logger
from users.models import Login


def get_feed(request):
    feed_url = settings.FEED_ADDRESS

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
        return redirect('forbidden')

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

    return render(request, 'post_create.html', context)

def delete_post(request, post_id):
    if not request.user.is_staff:
        return redirect('forbidden')
    elif post_id:
        post = Post.objects.get(pk=post_id)
        post.deleted = True
        post.save()
        if post.parent:
            return redirect('content:post_details', post_id=post.parent.pk)
        else:
            return redirect('index')
    return redirect('index')

def post_details(request, post_id):
    if post_id:
        post = get_object_or_404(Post, pk=post_id, deleted=False)
    else:
        return redirect('index')

    form = write_response_form(request.POST or None)
    if form.is_valid():
        response = form.save(commit=False)
        response.author = request.user
        response.parent = post
        response.title = 'Re: %s' % post.title
        form.save()
        return redirect('content:post_details', post_id=post.pk)

    deleted = Q(deleted=False)
    if not request.user.is_anonymous:
        deleted |= Q(author=request.user)
    query = Q(parent=post) & deleted
    responses = Post.objects.filter(query).order_by('-added')
    context = {
        'post': post,
        'responses': responses,
        'form': form
    }
    return render(request, 'post_details.html', context)
