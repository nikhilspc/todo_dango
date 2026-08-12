from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def home(request):
    tasks = Task.objects.filter(is_deleted=False).order_by('-id')
    return render(request, 'tasks/home.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'tasks/form.html', {'form': form})


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/form.html', {'form': form})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_deleted = True
    task.save()
    return redirect('home')