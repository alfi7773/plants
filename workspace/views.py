from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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
        form.instance.workspace = self.request.session.get('plant_id')  # Должно быть задано где-то раньше
        return super().form_valid(form)
    
    
class UpdatePlant(UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = 'workspace/update.html'
    
    def form_valid(self, form):
        plant_id = self.request.session.get('plant_id')
        if plant_id is not None:
            form.instance.workspace = get_object_or_404(Plant, id=plant_id)
        else:
            form.instance.workspace = None
            
        return super().form_valid(form)
            
    def get_success_url(self):
        return reverse_lazy('work')
    
    
class DeletePlant(DeleteView):
    model = Plant
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(reverse_lazy('work'))
    
    

# Create your views here.
