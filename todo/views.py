from datetime import datetime
from django.shortcuts import render, redirect

from .models import Todolist

# Create your views here.


def todo(request):
    todos = Todolist.objects.filter(done=False)
    frontend = {'todos': todos}
    return render(request, 'todo/todo.html', frontend)


def add(request):
    if request.method == 'POST':
        item = Todolist(item=request.POST['additem'])
        item.save()

    return redirect('/')


def edit(request, pk):
    if request.method == 'POST':
        task = Todolist.objects.get(pk=pk)
    
        task.item = request.POST['item']
        task.description = request.POST['description']
        task.save()

    return redirect('/')


def delete(request, pk):
    if request.method == 'POST':
        task = Todolist.objects.get(pk=pk)
        task.delete()

    return redirect('/')


def done(request, pk):
    task = Todolist.objects.get(pk=pk)
    task.done = True
    task.completed_on = datetime.now()
    task.save()

    return redirect('/')


def completed(request):
    tasks_done = Todolist.objects.filter(done=True)
    frontend = {'tasks_done': tasks_done}
    return render(request, 'todo/completed.html', frontend)


def restore(request, pk):
    task = Todolist.objects.get(pk=pk)
    task.done = False
    task.completed_on = None
    task.save()

    return redirect('/completed')