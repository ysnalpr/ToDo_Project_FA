from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),
    path('account/current/todo/', views.CurrentToDoList.as_view(), name='current_todo'),
    path('account/complete/todo/', views.CompleteToDoList.as_view(), name='complete_todo'),
    path('account/dashboard/', login_required(TemplateView.as_view(template_name="account/dashboard.html")), name='dashboard'),
    path('account/todo/add/', views.ToDoCreate.as_view(), name='todo_create'),
    path('account/todo/<int:pk>/edit/', views.ToDoUpdate.as_view(), name='todo_update'),
    path('account/todo/<int:pk>/detail/', views.TodoDetail.as_view(), name='todo_detail'),
    path('account/todo/<int:pk>/delete/', views.ToDoDelete.as_view(), name='todo_delete'),
    path('account/todo/<int:pk>/complete/', views.complete_todo, name='completetodo'),
]