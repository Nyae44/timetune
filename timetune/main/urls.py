from django.urls import path
from . import  views
app_name = 'main'
urlpatterns = [
    path('', views.home, name=""),
    
    path('register', views.register, name="register"),
    
    path('login', views.login, name="login"),
    
    path('logout', views.logout, name="logout"),
    
    # CRUD
    
    path('dashboard', views.dashboard, name="dashboard"),
    
    path('create-task', views.create_task, name="create-task"), 
    
    path('update-task/<int:pk>', views.update_task, name="update-task"),
    
    path('task/<int:pk>', views.singular_task, name="task"),
    
    
    
    
]
