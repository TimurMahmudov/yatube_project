from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'posts/index.html')

def group_posts(request):
    return HttpResponse('Группы постов')

def group_list(request, list_name):
    return HttpResponse(f'Посты в группе {list_name}')