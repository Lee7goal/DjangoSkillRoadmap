from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .models import TodoModel


# Create your views here.


class TodoIndexView(View):
    def get(self, request):
        obj = TodoModel.objects.all()[:10]
        context = {'obj': obj}
        return render(request, 'todo-app/index.html', context)

    def post(self, request):
        print(request.POST['todo'])
        print(request.user)
        new_todo = TodoModel.objects.create(short_text=request.POST['todo'])
        new_todo.save()
        # TodoModel.objects.create(short_text=request.GET[''])
        return HttpResponseRedirect('/todo')


def change_todo_status(request,todo_id):
    todo = TodoModel.objects.get(pk=todo_id)
    todo.is_finished = True
    todo.save()
    return HttpResponseRedirect('/todo')

