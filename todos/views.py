from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo, Priority


def main(request):
    latest_todo_list = Todo.objects.order_by('-prio', 'creation_date')
    context = {
        'latest_todo_list': latest_todo_list,
    }
    return render(request, 'todos/main.html', context)


def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todos/detail.html', {'todo': todo})


def priority(request, todo_id):
    return HttpResponse("You're looking at priority of todo {}".format(todo_id))


def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.job_rank = request.POST['job_rank']
    todo.imp_rank = request.POST['imp_rank']
    todo.prio = int(3 * int(request.POST['job_rank']) +
                    2 * int(request.POST['imp_rank']))
    todo.todo_text = request.POST['todo_text']
    todo.save()
    return redirect('/todos/')
