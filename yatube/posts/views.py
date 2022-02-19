from django.shortcuts import render, get_object_or_404


from .models import Post
from .models import Group

LIMIT_POST = 10


def index(request):
    template = 'posts/index.html'
    posts = group.posts.select_related('group')
    .all().order_by('-pub_date'
    )[:settings.LIMIT_POST]
    text = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'text': text,
    }
    return render(request, template, context)


def group_list(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    text = 'Лев Толстой – зеркало русской революции.'
    context = {
        'group': group,
        'posts': posts,
        'text': text,
    }
    return render(request, template, context)
