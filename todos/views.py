from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo, Priority


def main(request):
    latest_todo_list = Todo.objects.order_by('-creation_date')[:5]
    context = {
        'latest_todo_list': latest_todo_list,
    }
    return render(request, 'todos/main.html', context)


def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todos/detail.html', {'todo': todo})


def priority(request, todo_id):
    return HttpResponse("You're looking at priority of todo {}".format(todo_id))


def rank(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    try:
        selected_priority = todo.priority_set.get(pk=request.POST['priority'])
    except (KeyError, Priority.DoesNotExist):
        return render(request, 'todos/detail.html', {'todo': todo, 'error_message': "Didn't select a Prio"})
    else:
        selected_priority += 1
        selected_priority.save()
        return HttpResponseRedirect(reversed('todos:details', args=(todo.id)))
