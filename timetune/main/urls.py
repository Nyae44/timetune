from django.urls import path
from . import  views
app_name = 'main'
urlpatterns = [
    path('', views.home, name=""),
    
    path('register', views.register, name="register"),
    
    path('login', views.login, name="login"),
    
    path('logout', views.logout, name="logout"),
    
    path('dashboard', views.dashboard, name="dashboard"),
]
