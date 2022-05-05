from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    index_canal = 'posts/index.html'
    text = 'Это главная страница Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'text': text,
        'posts': posts,
    }
    return render(request, index_canal, context)

def group_posts(request):
    template = 'posts/group_list.html'
    group_info = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'group_info': group_info,
    }
    return render(request, template, context)
