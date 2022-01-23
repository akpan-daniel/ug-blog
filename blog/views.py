from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    context = {}
    return render(request, template_name, context)


def featured(request):
    pass


def latest(request):
    pass


def post_detail(request):
    pass


def search(request):
    pass


def author(request):
    pass


def archive(request):
    pass
