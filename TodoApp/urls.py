from django.urls import path
from .views import todo_index


urlpatterns = [
    path('', todo_index, name='todo-index')
]