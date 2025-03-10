from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from plant.models import *
from .forms import ImagePlantForm, PlantForm

class ListPlant(ListView):
    model = Plant
    template_name = 'workspace/index.html'
    context_object_name = 'plants'
    
    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)

class ProductCreateView(CreateView):
    model = Plant
    form_class = PlantForm
    template_name = 'workspace/create.html'
    success_url = reverse_lazy('work') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_form'] = ImagePlantForm()
        return context

    def form_valid(self, form):
        form.instance.workspace = self.request.session.get('plant_id')
        plant = form.save()

        image_form = ImagePlantForm(self.request.POST, self.request.FILES)
        if image_form.is_valid():
            for image in self.request.FILES.getlist('image'):
                ImagePlant.objects.create(plant=plant, image=image)

        return super().form_valid(form)
    
    
class UpdatePlant(UpdateView):
    model = Plant
    form_class = PlantForm
    template_name = 'workspace/update.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_form'] = ImagePlantForm()
        return context
    
    def form_valid(self, form):
        plant_id = self.request.session.get('plant_id')
        if plant_id is not None:
            form.instance.workspace = get_object_or_404(Plant, id=plant_id)
        else:
            form.instance.workspace = None

        if 'image' in self.request.FILES:
            for image in self.request.FILES.getlist('image'):
                ImagePlant.objects.create(plant=form.instance, image=image)

        form.save()
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
