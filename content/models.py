from django.db import models

# Create your models here.
from users.models import Login


class Post(models.Model):
    title = models.CharField(max_length=256, help_text='The title of the post')
    author = models.ForeignKey(Login, on_delete=models.CASCADE, help_text='Account that created this entry. In case it comes from another social network, it will use any system account')
    content = models.TextField(null=True, blank=True, help_text='The body of the post')
    reference = models.CharField(max_length=2048, help_text='Link to original post in case it comes from another social network')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, default=None, help_text='Foreign key to another post in case it is a response')

    added = models.DateTimeField(auto_now_add=True, help_text='Date when it was created on RagCP')
    updated = models.DateTimeField(auto_now=True, help_text='Date when modified')
