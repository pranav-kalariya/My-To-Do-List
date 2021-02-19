from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url as conf_url
from django.contrib.auth.views import logout_then_login
from todo_list_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('index/tasks/', views.tasks_list, name='tasks-list'),
    path('logout/', logout_then_login, {'login_url': 'index'}, name='logout'),
    path('index/messages/<int:user_todo>/', views.tasks_list, name='tasks-detail'),
    path('index/messages/delete/<int:user_todo>/', views.delete_tasks, name='taks-list-delete'),
]