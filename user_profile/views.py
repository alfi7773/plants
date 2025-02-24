from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LogoutView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'profile/signup.html'
    success_url = reverse_lazy('login')


class Login(LoginView):
    template_name = 'profile/login.html'
    success_url = reverse_lazy('/')
    
    

class CustomLogoutView(LogoutView):
    next_page = '/' 

# Create your views here.
