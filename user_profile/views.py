from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from .forms import CustomPasswordChangeForm, CustomUserCreationForm, LoginForm
from django.contrib.auth.views import LogoutView
from plant.models import Category, MyProfile, Plant
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from plant.models import Region
from django_countries import countries
from django.contrib import messages



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
    success_url = reverse_lazy('profile')
    
    # def get_success_url(self):
    #     return '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = self.get_form()  
        return context
    
    

class CustomLogoutView(LogoutView):
    next_page = '/' 
    
# class ProfileUser(ListView):
#     template_name = 'profile/profile.html'
#     model = Plant
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('home')
    
    
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect(self.success_url)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user'] = self.request.user
#         context['form'] = self.form_class()
#         return context
    
#     def get(self, request, *args, **kwargs):
#         cart = request.session.get('cart', {})
#         cart_items = []
#         total_price = 0
#         categories = Category.objects.all()
#         forms = self.form_class()

#         for plant_id, quantity in cart.items():
#             plant = Plant.objects.get(id=plant_id)
#             item_price = plant.price * quantity
#             cart_items.append({'product': plant, 'quantity': quantity, 'item_price': item_price})
#             total_price += item_price

#         context = {
#             'cart_items': cart_items,
#             'total_price': total_price,
#             'categories': categories,
#             'forms': forms,
#         }
        
#         return render(request, "profile/profile.html", context)




class ProfileUser(LoginRequiredMixin, View):
    template_name = 'profile/profile.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('home')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     context['user_form'] = self.form_class(instance=self.request.user)
    #     context['password_form'] = PasswordChangeForm(self.request.user)
    #     return context
    
    def get(self, request, *args, **kwargs):
        user_form = self.form_class(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)
        profile, created = MyProfile.objects.get_or_create(user=request.user)
        user_status = profile.status

        
        context = {
            'user_form': user_form,
            'password_form': password_form,
            'status': user_status,
            
        }
        print(f"User status: {user_status}")
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST, instance=request.user)
        password_form = PasswordChangeForm(request.user, request.POST)
        
        if 'user_form' in request.POST:
            if user_form.is_valid():
                user_form.save()
                return redirect('profile')
        elif 'password_form' in request.POST:
            if password_form.is_valid():
                messages.success(request, 'Success changed password')
                password_form.save()
                update_session_auth_hash(request, password_form.user) 
                return redirect('profile')
        
        context = {
            'user_form': user_form,
            'password_form': password_form
        }
        
        return render(request, self.template_name, context)


class RegionListView(LoginRequiredMixin, View):
    template_name = 'profile/adress.html'
    # model = User
    form_class = UserUpdateForm
    
    def get(self, request, *args, **kwargs):
        user_form = self.form_class(instance=request.user)
        password_form = PasswordChangeForm(request.user)
        profile, created = MyProfile.objects.get_or_create(user=request.user)
        user_status = profile.status
        context = {
            'user_form': user_form,
            'password_form': password_form,
            "countries": countries,
            'status': user_status,
        }
        return render(request, self.template_name, context)
    
    
    # def get(self, request, *args, **kwargs):
    #     country = request.GET.get("country")
    #     regions = Region.objects.filter(country=country).values("id", "name")
    #     return JsonResponse(list(regions), safe=False)

# Create your views here.
