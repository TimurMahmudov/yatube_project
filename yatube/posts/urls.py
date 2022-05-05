from django.urls import path
from . import views

app_name = 'posts_list'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('group/', views.group_posts, name = 'group_posts'),
]