from django.shortcuts import get_object_or_404, render

from .models import Group, Post

# Create your views here.


def index(request):
    text = 'Это главная страница Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'text': text,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group_info = 'Здесь будет информация о группах проекта Yatube'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group_info': group_info,
        'posts': posts,
        'group': group,
    }
    return render(request, 'posts/group_list.html', context)
