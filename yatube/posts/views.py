from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Главная страница')

def group_posts(request):
    return HttpResponse('Группы постов')

def group_list(request, list_name):
    return HttpResponse(f'Посты в группе {list_name}')