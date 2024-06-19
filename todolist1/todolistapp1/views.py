from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from. models import Task

# Create your views here.


def home(request):
    a=Task.objects.all()
    return render(request,'home.html',{'as':a})

def form(request):
    if request.method == 'POST':
        name=request.POST['name']
        task=request.POST['task']
        new_task=Task(Name=name,Task=task)
        new_task.save()
        return redirect('/home')
    
def edit(request,id):
    t=get_object_or_404(Task,id=id)
    if request.method == 'POST':
            name=request.POST['name']
            task=request.POST['task']
            t.Name=name
            t.Task=task
            t.save()
            return redirect('/home')
    return render(request,'edit.html',{'editss':t})
    
    
def delform(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('/home')

