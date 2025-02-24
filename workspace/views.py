from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from plant.models import *
from .forms import PlantForm

class ListPlant(ListView):
    model = Plant
    template_name = 'workspace/index.html'
    context_object_name = 'plants'

class ProductCreateView(CreateView):
    model = Plant
    form_class = PlantForm
    template_name = 'workspace/create.html'
    success_url = reverse_lazy('work') 

    def form_valid(self, form):
        form.instance.workspace = self.request.session.get('workspace_id')  # Должно быть задано где-то раньше
        return super().form_valid(form)
    
    
class DeletePlant(DeleteView):
    model = Plant
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(reverse_lazy('work'))
    
    

# Create your views here.
