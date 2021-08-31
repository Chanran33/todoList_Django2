from django.shortcuts import get_object_or_404, render,redirect
from django.utils import timezone
from .models import Todolist

# Create your views here.
def home(request):
    todos = Todolist.objects.all()
    return render(request,'home.html',{'todos':todos})

def create(request):
    new_todo = Todolist()
    new_todo.content = request.POST['content']
    new_todo.date = timezone.now()
    new_todo.save()
    return redirect('home')

def edit(request,id):
    edit_todo = Todolist.objects.get(id=id)
    return render(request,'edit.html',{'todo':edit_todo})

def update(request,id):
    update_todo = Todolist.objects.get(id=id)
    update_todo.content = request.POST['content']
    update_todo.date = timezone.now()
    update_todo.save()
    return redirect('home')

def delete(request,id):
    delete_todo = Todolist.objects.get(id=id)
    delete_todo.delete()
    return redirect('home')