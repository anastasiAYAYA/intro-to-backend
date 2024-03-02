from django.shortcuts import render, redirect
from .models import Todo, TodoList
from .forms import CreateList, CreateCategory


def index(request):
    return redirect('todo-lists')


def get_index(request):
    if request.method == 'GET':
        form = CreateCategory()
        todos = Todo.objects.all()
        categories = TodoList.objects.all()
        return render(request, 'todos/todo-lists.html', {'form': form, 'todos': todos, 'categories': categories})
    if request.method == 'POST':
        print(request.body)
        print(request.POST)

        form = CreateCategory(request.POST)

        if form.is_valid():
            title = form.data.get('Название')
            description = form.data.get('Описание')
            category = TodoList(title=title, description=description)
            category.save()
            return redirect(request.path)
        else:
            categories = TodoList.objects.all()
            return render(request, 'todos/todo-lists.html', {'categories': categories, 'form': form})


def get_category_info(request, pk):
    category = TodoList.objects.get(id=pk)
    todos = Todo.objects.filter(category_id=pk)
    if request.method == 'GET':
        form = CreateList()
        return render(request, 'todos/category_info.html', {'category': category, 'todos': todos, 'form': form})


def delete_category(request, pk):
    try:
        category = TodoList.objects.get(id=pk)
        category.delete()
        return redirect('/todo-lists/')
    except TodoList.DoesNotExist:
        return redirect('/todo-lists/')


def edit_category(request, pk):
    category = TodoList.objects.get(id=pk)
    todo = Todo.objects.filter(category_id=pk)
    form = CreateCategory(data={'Название': category.title, 'Описание': category.description})
    form2 = CreateList()

    if request.method == 'POST':
        form = CreateCategory(request.POST)
        form2 = CreateList(request.POST)
        if form.is_valid():
            title = form.data.get('Название')
            description = form.data.get('Описание')
            category.title = title
            category.description = description
            category.save()
            return redirect(f'/todo-lists/{category.id}')

        if form2.is_valid():
            title = form2.cleaned_data['Дело']
            description = form2.cleaned_data['Описание']
            due_date = form2.cleaned_data['Дата']
            status = form2.cleaned_data['Статус']
            todo = Todo.objects.create(title=title, description=description, due_date=due_date, status=status, category_id=pk)
            return redirect(f'/todo-lists/{category.id}')

    return render(request, 'todos/category_edit.html', {'category': category, 'form': form, 'todo': todo, 'form2': form2})


def get_info(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        return render(request, 'todos/todo_info.html', {'todo': todo})
    except Todo.DoesNotExist:
        return redirect('/todos/')


def delete_todo(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        category = todo.category
        todo.delete()
        return redirect(f'/todo-lists/{category.id}')
    except Todo.DoesNotExist:
        return redirect('/todo-lists/')


def edit_todo(request, pk):
    if request.method == 'GET':
        todo = Todo.objects.get(id=pk)
        form = CreateList(data={'Дело': todo.title, 'Описание': todo.description, 'Дата': todo.due_date,
                                'Статус': todo.status})

        return render(request, 'todos/edit-todo.html', {'todo': todo, 'form': form})
    if request.method == 'POST':
        todo = Todo.objects.get(id=pk)
        form = CreateList(request.POST)
        if form.is_valid():
            title = form.data.get('Дело')
            description = form.data.get('Описание')
            due_date = form.data.get('Дата')
            status = form.data.get('Статус') == 'on'
            todo.title = title
            todo.description = description
            todo.due_date = due_date
            todo.status = status
            category = todo.category
            todo.save()
            return redirect(f'/todo-lists/{category.id}')
