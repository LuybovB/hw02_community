from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render


from .models import Post
from .models import Group

LIMIT_POST = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
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
