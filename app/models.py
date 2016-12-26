from django.contrib.auth.models import User
from django.db import models


class Followers(models.Model):
    user = models.ForeignKey(User)
    id_str = models.CharField(max_length=200)
    screen_name = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
