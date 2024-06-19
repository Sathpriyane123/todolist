from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from. models import Task

# Create your views here.


def home(request):
    a=Task.object.all()
    return render(request,'home.html'{'a':a})

def form(request):
    if request.method == 'POST':
        name=request.POST['name']
        task=request.POST['task']
        new_task=Task(Name=name,Task=task)
        new_task.save()
        return render(request,'home.html')
    
def delform(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('home')

