from django.shortcuts import render

from .models import Post


def index(request):
    template_name = 'blog/index.html'
    posts = Post.objects.all().order_by('-published')
    featured = posts.filter(is_featured=True).order_by('-published')[:2]
    context = {
        'posts': posts[:6],
        'featured': featured
    }
    return render(request, template_name, context)


def post_create(request):
    template_name = 'blog/create.html'
    context = {}
    return(render, template_name, context)


def featured(request):
    pass


def latest(request):
    pass


def post_detail(request, slug):
    pass


def search(request):
    pass


def author(request):
    pass


def archive(request):
    pass
