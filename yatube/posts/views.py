from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


from .models import Post, Group, User

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


def profile(request, username):
    template = 'posts/profile.html'
    user_db = get_object_or_404(User, username=username)
    posts = user_db.posts.all()
    posts_count = posts.count
    page_obj = Paginator(posts, 10)
    context = {
        'posts_count': posts_count,
        'user_db': user_db,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, template, context)
