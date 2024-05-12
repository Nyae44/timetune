from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
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
    
    
    return render(request, "main/dashboard.html")











# User logout
 
def logout(request):
    auth.logout(request)
    
    return redirect("main:login")
