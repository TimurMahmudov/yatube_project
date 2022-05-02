from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('group/', views.group_posts),
    path('group/<slug:list_name>/', views.group_list),
]