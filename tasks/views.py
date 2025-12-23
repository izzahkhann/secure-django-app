from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.owner = request.user
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id, owner=request.user)
    task.delete()
    return redirect('task_list')
