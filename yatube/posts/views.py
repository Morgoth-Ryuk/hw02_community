from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()
QUANTITY_OF_POSTS_ON_PAGE = 10


def authorized_only(func):
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('/auth/login/')        
    return check_user

@login_required
def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, QUANTITY_OF_POSTS_ON_PAGE) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context) 

@authorized_only
def groups(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all().order_by('-pub_date')
    paginator = Paginator(post_list, QUANTITY_OF_POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)

def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author = author).order_by('-pub_date')
    post_count = Post.objects.filter(author = author).count()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/profile.html'
    context = {
        'author': author,
        'post_list': post_list,
        'page_obj': page_obj,
        'post_count': post_count
    }
    return render(request, template, context)

# Здесь код не доделан
def post_detail(request, post_id):
    # Здесь код запроса к модели и создание словаря контекста
    template = 'posts/post_detail.html'
    post = Post.objects.get(id = post_id)
    post_count = Post.objects.filter(author_id = post.author.id)
    author = post.author

    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context) 
