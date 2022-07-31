from django.urls import path
from .views import TodoIndexView, change_todo_status

urlpatterns = [
    path('', TodoIndexView.as_view(), name='todo-index'),
    path('<int:todo_id>/finished/', change_todo_status, name='finish-todo')
]
