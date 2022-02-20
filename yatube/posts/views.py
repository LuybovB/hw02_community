from django.shortcuts import render, get_object_or_404


from .models import Post
from .models import Group

LIMIT_POST = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    text = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'text': text,
    }
    return render(request, template, context)


def group_list(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    text = 'Лев Толстой – зеркало русской революции.'
    posts = group.posts.select_related(
        'group'
    ).all().order_by(
        '-pub_date'
    )[:LIMIT_POST]
    context = {
        'group': group,
        'posts': posts,
        'text': text,
    }
    return render(request, template, context)
