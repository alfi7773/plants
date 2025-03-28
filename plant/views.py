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
        
        # category = self.request.GET.get('category')
        # if category:
        #     plants = plants.filter(category_id=category)
        
        sizes = self.request.GET.getlist('size')
        if sizes:
            plants = plants.filter(sizes__id__in=sizes)
        
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
    
class ForLogin(ListView):
    template_name = 'for_login.html'
    context_object_name = 'plants'
    paginate_by = 9
    
    def get_queryset(self):
        plants = Plant.objects.all()
        self.plantfilter = PlantFilter(self.request.GET, queryset=plants)
        
        query = self.request.GET.get('q')
        if query:
            return Plant.objects.filter(name__icontains=query)
        
        # category = self.request.GET.get('category')
        # if category:
        #     plants = plants.filter(category_id=category)
        
        sizes = self.request.GET.getlist('size')
        if sizes:
            plants = plants.filter(sizes__id__in=sizes)
        
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


class NewArrivals(ListView):
    template_name = 'arrivval.html'
    context_object_name = 'plants'
    paginate_by = 9
    
    def get_queryset(self):
        plants = Plant.objects.filter(created_at='2025-03-05')
        self.plantfilter = PlantFilter(self.request.GET, queryset=plants)
        
        query = self.request.GET.get('q')
        if query:
            return Plant.objects.filter(name__icontains=query)
        
        # category = self.request.GET.get('category')
        # if category:
        #     plants = plants.filter(category_id=category)
        
        sizes = self.request.GET.getlist('size')
        if sizes:
            plants = plants.filter(sizes__id__in=sizes)
        
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
        context['form'] = CustomUserCreationForm
        context['forms'] = LoginForm
        context['filter'] = self.plantfilter
        return context

class CartView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        cart_items = []
        total_price = 0
        categories = Category.objects.all()
        plants = Plant.objects.all()

        for plant_id, quantity in cart.items():
            plant = get_object_or_404(Plant, id=int(plant_id))
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

class AddToCartView(View, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        plant_id = request.POST.get('plant_id')
        quantity = int(request.POST.get('quantity', 1))
        plant = get_object_or_404(Plant, id=plant_id)
        cart = request.session.get('cart', {})

        if str(plant_id) in cart:
            cart[str(plant_id)] += quantity
        else:
            cart[str(plant_id)] = quantity

        request.session['cart'] = cart
        request.session.modified = True
        return redirect('/cart/')

class RemoveFromCartView(View):
    def post(self, request, *args, **kwargs):
        plant_id = request.POST.get('plant_id')
        cart = request.session.get('cart', {})

        if str(plant_id) in cart:
            del cart[str(plant_id)]
            request.session['cart'] = cart
            request.session.modified = True

        return redirect('/cart/')

class DetailPlant(DetailView):
    model = Plant
    context_object_name = 'plant'
    template_name = 'detail_plant.html'
    
    def get_context_data(self, **kwargs):
        plant = self.get_object()
        context = super().get_context_data(**kwargs)
        context['sizes'] = plant.sizes.all()
        context['categories'] = Category.objects.all()
        context['tags'] = plant.tags.all()
        context['plants'] = Plant.objects.all()
        context['images'] = plant.images.all()
        context['form'] = CustomUserCreationForm
        context['forms'] = LoginForm
        
        return context
    
class Reviews(DetailView):
    model = Plant
    context_object_name = 'plant'
    template_name = 'reviews.html'
    
    def get_context_data(self, **kwargs):
        plant = self.get_object()
        context = super().get_context_data(**kwargs)
        context['sizes'] = plant.sizes.all()
        context['categories'] = Category.objects.all()
        context['tags'] = plant.tags.all()
        context['plants'] = Plant.objects.all()
        context['images'] = plant.images.all()
        context['form'] = CustomUserCreationForm
        context['forms'] = LoginForm
        
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomUserCreationForm
        context['forms'] = LoginForm
        return context
    
    
class AllBlogs(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blogs.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomUserCreationForm
        context['forms'] = LoginForm
        return context
    
    
class CreateOrderView(View, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user).first()
        cart_items = CartItem.objects.filter(cart=cart)
        
        total_price = sum(item.get_total() for item in cart_items)
        
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            status='pending', 
        )


        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                plant=item.plant,
                quantity=item.quantity,
                price=item.plant.price,
            )

        cart_items.delete()


        return redirect('order_detail', order.id)  


class OrderDetailView(View, LoginRequiredMixin):  
    def get(self, request, *args, **kwargs): 
        order_id = kwargs.get('order_id') 
        # order = Order.objects.filter(user=request.user).first()
        order = Order.objects.filter(user=request.user, id=order_id).first()
        if order is None:  
            return redirect('cart')  
        
        print(f"Order ID: {order.id} - Total price: {order.total_price}")

        order_items = OrderItem.objects.filter(order=order) 

        context = {  
            'order': order,  
            'order_items': order_items,  
        }  
        return render(request, 'order/order_detail.html', context)  
