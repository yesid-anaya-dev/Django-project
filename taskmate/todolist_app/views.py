from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages


# Create your views here.
# def todolist(request):
#     return HttpResponse("Welcome to Task Page")

def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("New Task Added!!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all

        context = {
            'task_text': 'Welcome to the Task App.',
            'all_tasks': all_tasks
            }
        return render(request, 'task.html', context)


def about(request):
    context = {'about_text': 'Welcome to About page.'}
    return render(request, 'about.html', context)


def contact(request):
    context = {'contact_text': 'Welcome to the Contact page.'}
    return render(request, 'contact.html', context)
