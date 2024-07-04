from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def todolist(request):
#     return HttpResponse("Welcome to Task Page")

def todolist(request):
    context = {'task_text': 'Welcome to the Task App.'}
    return render(request, 'task.html', context)


def about(request):
    context = {'about_text': 'Welcome to About page.'}
    return render(request, 'about.html', context)


def contact(request):
    context = {'contact_text': 'Welcome to the Contact page.'}
    return render(request, 'contact.html', context)
