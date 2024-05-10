from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm
# Create your views here.
def home(request):
    
    
    return render(request, 'main/index.html')

# Register a user
def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        
        
        if form.is_valid():
            form.save()
            
        # return redirect()
    context = {'form':form}
    
    return render(request, "main/register.html", context=context)

# Login a user
