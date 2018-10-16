from django.shortcuts import render
from django.views import generic
from .models import TodoItem, TodoList
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class IndexView(generic.ListView):
    model = TodoList
    template_name = 'todolist/index.html'


class ListDetailView(generic.DetailView):
    model = TodoList
    template_name = 'todolist/TodoList_detail.html'



def result(request, todolist_id):
    print(todolist_id)
    todolist = TodoList.objects.get(id=todolist_id)

    return HttpResponse(f"Completed {todolist.completed} item/s from the list ({todolist.title})")




def submitForm(request, todolist_id):
    list_ = request.POST.getlist('checks')
    print(list_)
    todolist = TodoList.objects.get(id=todolist_id)
    todolist.completed = len(list_)
    todolist.save()


    return HttpResponseRedirect(reverse('todolist:result', args=(todolist.id,)))

#reverse('todolist:result', args=(todolist.id,))
