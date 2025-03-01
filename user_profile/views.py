from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.views import LogoutView
from plant.models import Plant
from django.contrib.auth import login
from django.http import JsonResponse

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'profile/signup.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
    

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
    form_class = LoginForm
    template_name = 'profile/login.html'
    success_url = reverse_lazy('home')
    
    # def get_success_url(self):
    #     return '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = self.get_form()  
        return context
    
    

class CustomLogoutView(LogoutView):
    next_page = '/' 
    
class ProfileUser(ListView):
    template_name = 'profile/profile.html'
    model = Plant
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    

# Create your views here.
