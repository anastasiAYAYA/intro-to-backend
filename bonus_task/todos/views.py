from django.shortcuts import render, redirect
from .models import Todo
from django.core.paginator import Paginator
from django.db.models import Q


sizes = [5, 10, 20]


def index(request):
    return redirect('todos')


def get_todos(request):
    size = request.GET.get('size', 10)
    page = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', 'title')
    title = request.GET.get('title', '')
    todos = Todo.objects.filter(Q(title__icontains=title)).order_by(order_by)

    filters = {
        'title': title
    }

    paginator = Paginator(todos, size)
    page_obj = paginator.get_page(page)
    if request.method == 'GET':
        return render(request, 'todos/todos.html', {'sizes': sizes, 'page_obj': page_obj,
                                                    'paginator': paginator, 'order_by': order_by, 'filters': filters})


def get_info(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        return render(request, 'todos/todo_info.html', {'todo': todo})
    except Todo.DoesNotExist:
        return redirect('/todos/')
