from django.urls import path
from . import  views
app_name = 'main'
urlpatterns = [
    path('', views.home, name=""),
    
    path('register', views.register, name="register"),
]
