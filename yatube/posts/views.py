from django.shortcuts import render, get_object_or_404
from .models import Post, Group


QUANTITY_OF_POSTS_ON_PAGE = 10


def index(request):
    posts = Post.objects.order_by(
        '-pub_date')[:QUANTITY_OF_POSTS_ON_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def groups(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by(
        '-pub_date')[:QUANTITY_OF_POSTS_ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
