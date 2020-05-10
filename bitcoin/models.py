from django.db import models

# Create your models here.
from ragcp import settings


class Wallet(models.Model):
    identifier = models.TextField(primary_key=True)
    password = models.TextField()

    @property
    def service_url(self):
        return settings.host
