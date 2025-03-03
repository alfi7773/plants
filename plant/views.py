from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from .models import Plant
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import *
from django.views.generic import TemplateView, ListView, DetailView
from .filter import PlantFilter
from django.core.paginator import Paginator
from user_profile.forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

  

class HomePageView(ListView):
    template_name = 'landing.html'
    context_object_name = 'plants'
    paginate_by = 9
    
    def get_queryset(self):
        plants = Plant.objects.all()
        self.plantfilter = PlantFilter(self.request.GET, queryset=plants)
        
        query = self.request.GET.get('q')
        if query:
            return Plant.objects.filter(name__icontains=query)
        
        return self.plantfilter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        context['categories'] = Category.objects.annotate(plant_count=Count('plant'))
        context['sizes'] = Size.objects.annotate(plant_count=Count('plant'))
        context['size_objects'] = Size.SMALL, Size.MEDIUM, Size.LARGE
        context['form'] = CustomUserCreationForm
        context['forms'] = LoginForm
        context['filter'] = self.plantfilter
        return context
    
class Catologue(ListView):
    template_name = 'catologue.html'
    context_object_name = 'plants'
    paginate_by = 9
    
    def get_queryset(self):
        plants = Plant.objects.all()
        self.plantfilter = PlantFilter(self.request.GET, queryset=plants)
        
        query = self.request.GET.get('q')
        if query:
            return Plant.objects.filter(name__icontains=query)
        
        return self.plantfilter.qs
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(plant_count=Count('plant'))
        context['sizes'] = Size.objects.annotate(plant_count=Count('plant'))
        context['size_objects'] = Size.SMALL, Size.MEDIUM, Size.LARGE
        context['filter'] = self.plantfilter
        return context


class CartView(View):
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        cart_items = []
        total_price = 0
        categories = Category.objects.all()
        plants = Plant.objects.all()

        for plant_id, quantity in cart.items():
            plant = Plant.objects.get(id=plant_id)
            item_price = plant.price * quantity
            cart_items.append({'product': plant, 'quantity': quantity, 'item_price': item_price})
            total_price += item_price

        context = {
            'cart_items': cart_items,
            'total_price': total_price,
            'categories': categories,
            'plants': plants,
        }
        
        
        
        return render(request, 'cart/cart.html', context)


class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        plant_id = request.POST.get('plant_id')
        quantity = int(request.POST.get('quantity', 1))

        plant = get_object_or_404(Plant, id=plant_id)

        cart = request.session.get('cart', {})

        if plant_id in cart:
            cart[plant_id] += quantity
        else:
            cart[plant_id] = quantity

        request.session['cart'] = cart

        return redirect('/cart/')


class RemoveFromCartView(View):
    def post(self, request, *args, **kwargs):
        plant_id = request.POST.get('plant_id')  

        cart = request.session.get('cart', {})

        if plant_id in cart:
            del cart[plant_id]
            request.session['cart'] = cart
            return redirect('/cart/')
        else:
            return JsonResponse({'success': False, 'message': 'Товар не найден в корзине!'})

class DetailPlant(DetailView):
    model = Plant
    context_object_name = 'plant'
    template_name = 'detail_plant.html'
    
    def get_context_data(self, **kwargs):
        plant = self.get_object()
        context = super().get_context_data(**kwargs)
        context['sizes'] = plant.sizes.all()
        context['categories'] = Category.objects.all()
        context['plants'] = Plant.objects.all()
        
        return context
    

class AddRating(LoginRequiredMixin, View):
    def post(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk)
        score = int(request.POST.get('score', 0))

        if 1 <= score <= 5:
            Rating.objects.update_or_create(
                user=request.user, plant=plant, defaults={'score': score}
            )

        return redirect('detail_plant', pk=plant.pk)
    
class DetailBlog(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'detail_blog.html'
    
class AllBlogs(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blogs.html'