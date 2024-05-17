from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateTaskForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import Task
def home(request):
    
    
    return render(request, 'main/index.html')

# Register a user
def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            
        return redirect('main:login')
    context = {'form':form}
    
    return render(request, "main/register.html", context=context)

# Login a user

def login(request):
    form = LoginForm()
    
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            # Check if the user exists
            
            if user is not None:
                
                auth.login(request, user)
                
                return redirect('main:dashboard')
    context={'form2':form}
    
    return render(request, "main/login.html", context=context)


# Dashboard

@login_required(login_url='main:login')
def dashboard(request):
    
    my_tasks = Task.objects.all()
    context = {'tasks':my_tasks}
    return render(request, "main/dashboard.html", context=context)

# Add a Task

@login_required(login_url='main:login')
def create_task(request):
    
    form = CreateTaskForm()
    
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect("main:dashboard")
    
    context={'form':form}
    return render(request, "main/create-task.html", context=context)

# Update task
@login_required(login_url='main:login')
def update_task(request, pk):
    
    task = Task.objects.get(id=pk)

    
    form = UpdateTaskForm(instance=task)
    
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=task)
        
        if form.is_valid():
            
            form.save()
            
            return redirect("main:dashboard")
        
    context = {'form':form}
    
    return render(request, "main/update-task.html", context=context)
            
            
    
# Read / view a singular task
@login_required(login_url="main:login")
def singular_task(request, pk):
    
    all_tasks = Task.objects.get(id=pk)
    
    context ={'task':all_tasks}
    return render(request, "main/view-task.html",context=context )








# User logout
 
def logout(request):
    auth.logout(request)
    
    return redirect("main:login")
