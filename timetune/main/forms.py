from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task

from django import forms
from django.forms.widgets import PasswordInput, TextInput

# - Register/Create User

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']
        

# -Login  a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
# - Add a Task
class CreateTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'completed']
        
# - Update Task

class UpdateTaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'completed']
        
    
    