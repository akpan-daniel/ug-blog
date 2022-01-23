from django.db import models

from users.models import User

from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    CHOICES = ()
    title = models.CharField(max_length=250)
    overview = models.CharField(max_length=300)
    slug = models.SlugField(max_length=250)
    thumbnail = models.ImageField(upload_to='thumbnail')
    content = RichTextUploadingField()
    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='posts')
    tags = models.ManyToManyField('Tag', related_name='posts')
    is_featured = models.BooleanField(default=False)
    has_poll = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    upvotes = models.ManyToManyField(User, related_name='upvotes', blank=True)
    downvotes = models.ManyToManyField(
        User, related_name='downvotes', blank=True)
    published = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    @property
    def get_upvotes(self) -> int:
        return self.upvotes.count()

    @property
    def get_downvotes(self) -> int:
        return self.downvotes.count()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Moderator(models.Model):
    user = models.ForeignKey(
        User, related_name='moderates', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name='moderators', on_delete=models.CASCADE)
