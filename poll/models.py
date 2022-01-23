from django.db import models

from users.models import User
from blog.models import Post


class Poll(models.Model):
    question = models.CharField(max_length=200)
    post = models.OneToOneField(
        Post, related_name='poll', on_delete=models.CASCADE)
    is_open = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.question


class Option(models.Model):
    choice = models.CharField(max_length=50)
    poll = models.ForeignKey(
        Poll, related_name='option', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, blank=True)

    @property
    def get_count(self) -> int:
        return self.users.count()

    def __str__(self) -> str:
        return self.choice
