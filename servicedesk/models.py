from django.db import models
from ragcp.models import Login

# Create your models here.

class Categories(models.Model):
    name = models.TextField(default='No name set', null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Ticket(models.Model):
    STATES = (
        (1, 'Open'),
        (2, 'Closed'),
        (3, 'Accepted'),
        (4, 'Cannot reproduce'),
        (5, 'Rejected'),
        (6, 'Invalid'),
        (7, 'No proofs'),
    )
    created_by = models.ForeignKey(Login, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subject = models.CharField(max_length=128, default='', null=False)
    body = models.TextField(default='', null=False)
    state = models.IntegerField(default=1, null=False, choices=STATES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def latest_reply(self):
        reply = Replies.objects.filter(ticket=self).latest('created')
        return reply

    @property
    def state_str(self):
        for state in self.STATES:
            if state[0] == self.state:
                return state[1]
        return None


class Replies(models.Model):
    created_by = models.ForeignKey(Login, on_delete=models.CASCADE)
    body = models.TextField(default='', null=False)
    response_needed = models.BooleanField(default=False, null=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
