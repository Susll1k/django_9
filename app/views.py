from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Todo

def show_task(request):
    tasks = Todo.objects.all()
    if request.method == 'POST':
        tasks = Todo.objects.filter(title = request.POST['title'])
        if request.POST['title'] == '':
            tasks = Todo.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        try:
            if request.POST['completed'] == 'True':
                tasks = Todo.objects.create(title = request.POST['title'], description = request.POST['description'], completed = request.POST['completed'])
        except:
                tasks = Todo.objects.create(title = request.POST['title'], description = request.POST['description'], completed = False)
        return redirect(reverse('tasks'))
    return render(request, 'create.html')

def update_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    if request.method == 'POST':
        try:
            if request.POST['completed'] == 'True':
                task.title = request.POST['title']
                task.description = request.POST['description']
                task.completed = request.POST['completed']
        except:
                task.title = request.POST['title']
                task.description = request.POST['description']
                task.completed = False
        task.save()
        return redirect(reverse('tasks'))
    return render(request, 'update.html')

def delete_task(request, task_id):
    task = Todo.objects.get(id=task_id)
    task.delete()
    return redirect(reverse('tasks'))


def home(request):
    return render(request, 'home.html')