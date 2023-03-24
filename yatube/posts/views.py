from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


QUANTITY_OF_POSTS_ON_PAGE = 10


def authorized_only(func):
    # Функция-обёртка в декораторе может быть названа как угодно
    def check_user(request, *args, **kwargs):
        # В любую view-функцию первым аргументом передаётся объект request,
        # в котором есть булева переменная is_authenticated,
        # определяющая, авторизован ли пользователь.
        if request.user.is_authenticated:
            # Возвращает view-функцию, если пользователь авторизован.
            return func(request, *args, **kwargs)
        # Если пользователь не авторизован — отправим его на страницу логина.
        return redirect('/auth/login/')        
    return check_user

@login_required
def index(request):
    posts = Post.objects.order_by(
        '-pub_date')[:QUANTITY_OF_POSTS_ON_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@authorized_only
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
