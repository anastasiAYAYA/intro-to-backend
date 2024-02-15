from django.shortcuts import render, redirect
from .models import Todo
from .forms import CreateList


def get_index(request):
    return render(request, 'todos/index.html')


def get_list(request):
    if request.method == 'GET':
        form = CreateList()
        todos = Todo.objects.all()
        return render(request, 'todos/todos.html', {'form': form, 'todos': todos})
    if request.method == 'POST':
        print(request.body)
        print(request.POST)
        # title = request.POST.get('title', '')
        # description = request.POST.get('description', '')
        # due_date = request.POST.get('due_date', '2024-02-08')
        # status = request.POST.get('status') == 'on'

        form = CreateList(request.POST)

        if form.is_valid():
            title = form.data.get('Дело')
            description = form.data.get('Описание')
            due_date = form.data.get('Дата')
            status = form.data.get('Статус') == 'on'
            todo = Todo(title=title, description=description, due_date=due_date, status=status)
            todo.save()
            return redirect(request.path)
        else:
            todos = Todo.objects.all()
            return render(request, 'todos/todos.html', {'todos': todos, 'form': form})


def get_info(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        return render(request, 'todos/todo_info.html', {'todo': todo})
    except Todo.DoesNotExist:
        return redirect('/todos/')


def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('/todos/')
    except Todo.DoesNotExist:
        return redirect('/todos/')

