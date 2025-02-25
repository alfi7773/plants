from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LogoutView
from django.http import JsonResponse

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'profile/signup.html'
    success_url = reverse_lazy('login')

# def register(request):
#     if request.method == "POST":
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({"success": True})  # Закроем модалку в JS
#         return JsonResponse({"success": False, "errors": form.errors})  # Вернем ошибки

#     form = CustomUserCreationForm()
#     return render(request, "profile/register.html", {"form": form})

class Login(LoginView):
    template_name = 'profile/login.html'
    success_url = reverse_lazy('/')
    
    

class CustomLogoutView(LogoutView):
    next_page = '/' 

# Create your views here.
