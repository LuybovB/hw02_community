from django.shortcuts import render, get_object_or_404


from .models import Post
from .models import Group

LIMIT_POST = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.select_related('group').all()[:LIMIT_POST]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_list(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:LIMIT_POST]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
