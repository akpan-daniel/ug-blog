import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


def upload_path(instance, filename):
    filename, ext = os.path.splitext(filename)
    filename = "{0}{1}".format(int(timezone.now().timestamp()), ext)
    return "user/upload/avatar/{0}".format(filename)


class User(AbstractUser):
    picture = models.ImageField(
        default='default.png', upload_to=upload_path)
    bio = models.TextField(max_length=300, blank=True)
    location = models.CharField(max_length=30, blank=True)
