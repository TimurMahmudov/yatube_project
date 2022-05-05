from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    index_canal = 'posts/index.html'
    text = 'Это главная страница Yatube'
    context = {
        'text': text,
    }
    return render(request, index_canal)

def group_posts(request):
    template = 'posts/group_list.html'
    context = {
        'group_info': template,
    }
    return render(request, template)
