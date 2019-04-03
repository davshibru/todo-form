from django.urls import path
from . import views


urlpatterns = [
    path('', views.todo_list, name='todo_list' ),
    path('todo/<int:pk>/edit', views.todo_edit, name='todo_edit'),
    path('todo/new/', views.todo_new, name='todo_new'),
]
