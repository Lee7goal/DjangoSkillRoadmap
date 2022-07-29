from django.shortcuts import render
from .models import TodoModel

# Create your views here.
def todo_index(request):
    obj = TodoModel.objects.all()[:10]
    context = {'obj': obj}
    return render(request, 'todo-app/index.html', context)
