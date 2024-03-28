from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect

from .models import Todo
from .forms import CreateList

sizes = [5, 10, 20]


def get_index(request):
    return redirect('todo-list')


def get_todos(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = CreateList()
            todos = Todo.objects.filter(user=request.user)
            return render(request, 'todos/todos.html', {'form': form, 'todos': todos})
        if request.method == 'POST':
            form = CreateList(request.POST)

            if form.is_valid():
                title = form.cleaned_data.get('Todo')
                description = form.cleaned_data.get('Description')
                due_date = form.cleaned_data.get('Date')
                status = form.cleaned_data.get('Status')

                todo = Todo.objects.create(
                    title=title,
                    description=description,
                    due_date=due_date,
                    status=status,
                    user=request.user
                )
                return redirect(request.path)
            else:
                todos = Todo.objects.filter(user=request.user)
                return render(request, 'todos/todos.html', {'todos': todos, 'form': form})
    else:
        return redirect('/auth/login/')


def delete_todo(request, pk):
    if request.user.is_authenticated:
        todo = get_object_or_404(Todo, pk=pk, user=request.user)
        todo.delete()
        return redirect('/todos/')
    else:
        return redirect('/todos/')


def get_info(request, pk):
    if request.user.is_authenticated:
        try:
            todo = get_object_or_404(Todo, pk=pk, user=request.user)
            return render(request, 'todos/todo_info.html', {'todo': todo})
        except Todo.DoesNotExist:
            return redirect('/todos/todo-list/')
    else:
        return redirect('/todos/todo-list/')


def get_todo_list(request):
    size = request.GET.get('size', 10)
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', 'title')
    title = request.GET.get('title', '')

    if request.user.is_authenticated:
        current_user = request.user
        todos = Todo.objects.filter(user=current_user, title__icontains=title).order_by(order_by)
    else:
        todos = Todo.objects.all()

    filters = {
        'title': title
    }

    paginator = Paginator(todos, size)
    page_obj = paginator.get_page(page)
    if request.method == 'GET':
        return render(request, 'todos/todo-list.html', {'sizes': sizes, 'page_obj': page_obj,
                                                        'paginator': paginator, 'order_by': order_by,
                                                        'filters': filters, 'todos': todos})
