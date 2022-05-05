from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    index_canal = 'posts/index.html'
    text = 'Это главная страница Yatube'
    context = {
        'text': text,
    }
    return render(request, index_canal, context)

def group_posts(request):
    template = 'posts/group_list.html'
    group_info = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'group_info': group_info,
    }
    return render(request, template, context)
