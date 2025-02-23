from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, ListView
from .filter import PlantFilter
from django.core.paginator import Paginator


class HomePageView(ListView):
    model = Plant
    template_name = 'landing.html'
    context_object_name = 'plants'
    paginate_by = 4
    
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PlantFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset 
        return context
    
    



