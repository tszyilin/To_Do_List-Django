from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks = Task.objects.all() # Grab everything
    forms = TaskForm()

    # Save the input to the django database
    if request.method == "POST":
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/') # Will go back to the same page
        

    content_dic = {'tasks': tasks, 'forms': forms} # Put the data into a dictionary

    return render(request, 'list.html', content_dic) # The last argument must be a dictionary


def update_task(request, pk):   #pk is for primary key
    tasks = Task.objects.get(id=pk)
    forms = TaskForm(instance=tasks)

    if request.method == "POST":
        forms = TaskForm(request.POST, instance=tasks)
        if forms.is_valid():
            forms.save()
            return (redirect('/'))
    
    content_dic = {'forms': forms }
    return render(request, 'update_task.html', content_dic)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')

    content_dic = {'item': item}
    return render(request, 'delete.html', content_dic)