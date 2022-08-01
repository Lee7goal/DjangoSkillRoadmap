from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from .models import TodoModel


# Create your views here.


class TodoIndexView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self, request):
        obj = TodoModel.objects.filter(create_by=request.user).all()[:10]
        context = {'obj': obj}
        print(type(request.user))
        return render(request, 'todo-app/index.html', context)

    @method_decorator(login_required(login_url='login'))
    def post(self, request):
        print(request.POST['todo'])
        print(request.user)
        new_todo = TodoModel.objects.create(short_text=request.POST['todo'], create_by=request.user)
        new_todo.save()
        # TodoModel.objects.create(short_text=request.GET[''])
        return HttpResponseRedirect('/todo')


def change_todo_status(request,todo_id):
    todo = TodoModel.objects.get(pk=todo_id)
    todo.is_finished = True
    todo.save()
    return HttpResponseRedirect('/todo')

