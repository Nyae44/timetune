from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
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
                
                # return redirect('')
    context={'form2':form}
    
    return render(request, "main/login.html", context=context)
