from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView, DetailView
from .filter import PlantFilter
from django.core.paginator import Paginator
  

class HomePageView(ListView):
    template_name = 'landing.html'
    context_object_name = 'plants'
    paginate_by = 4
    
    def get_queryset(self):
        plants = Plant.objects.all()
        self.plantfilter = PlantFilter(self.request.GET, queryset=plants)
        return self.plantfilter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        context['categories'] = Category.objects.all()
        context['filter'] = self.plantfilter
        return context
    
class DetailPlant(DetailView):
    model = Plant
    context_object_name = 'plant'
    template_name = 'detail_plant.html'
    
class DetailBlog(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'detail_blog.html'