from django.urls import path
from . import views

app_name = 'colorir'
urlpatterns = [
    path('', views.loginview, name='login'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home')
]
