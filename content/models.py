import requests
from django.db import models

# Create your models here.
from ragcp.settings import logger
from users.models import Login


class Post(models.Model):
    title = models.CharField(max_length=256, help_text='The title of the post')
    author = models.ForeignKey(Login, on_delete=models.CASCADE,
                               verbose_name='Created by',
                               help_text='Account that created this entry. In case it comes from another social network, it will use any system account')
    content = models.TextField(null=True, blank=True,
                               help_text='The body of the post')
    reference = models.CharField(max_length=2048, null=True, default=None,
                                 help_text='Link to original post in case it comes from another social network')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                               default=None, verbose_name='In response to',
                               help_text='Foreign key to another post in case it is a response')
    deleted = models.BooleanField(default=False, null=True)

    added = models.DateTimeField(auto_now_add=True,
                                 help_text='Date when it was created on RagCP')
    updated = models.DateTimeField(auto_now=True,
                                   help_text='Date when modified')
    scoring = models.FloatField(max_length=28, null=True, default=None)
    scoring_label = models.CharField(max_length=64, default=None, null=True)

    def __str__(self):
        return '%s: %s by %s' % (
        self.title[:10], self.content[:40], self.author.username)

    def analyze_content(self):
        uri = 'https://natural-language-understanding-demo.ng.bluemix.net/api/analyze'
        headers = {
            'Content-Type': 'application/json'
        }
        data = '{"features": {"sentiment": {}},"text": "%s"}' % self.content
        results = requests.post(uri, data=data, headers=headers)
        if results.status_code == 200:
            results = results.json()['results']['sentiment']['document']
            return results
        else:
            logger.warning('There was a problem analyzing post %s, %s' % (self.id, results))
            return {'score': 0, 'label': 'neutral', 'error': True}

    @property
    def sentiment_score(self):
        return self.analyze_content()['score']

    @property
    def sentiment_label(self):
        return self.analyze_content()['label']

    @property
    def sentiment(self):
        return self.analyze_content()

    def save(self, **kwargs):
        if self.parent is not None:
            analysis = self.analyze_content()
            print(analysis)
            scoring = analysis['score']
            label = analysis['label']

            if 'error' in analysis:
                super(Post, self).save()

            if scoring >= 0:
                self.deleted = True
            self.scoring = scoring
            self.scoring_label = label
        super(Post, self).save()

    @property
    def num_responses(self):
        return Post.objects.filter(parent=self.pk, deleted=False).count()
