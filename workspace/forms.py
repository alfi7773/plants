from plant.models import *
from django import forms

class PlantForm(forms.ModelForm):
    
    class Meta:
        model = Plant
        fields = ['name', 
                  'price', 
                  'short_description', 
                  'sizes', 
                  'category', 
                  'tags', 
                  'description', 
                #   'image',
                  'user']
        
    widgets = {
        'name': forms.TextInput(attrs={'class': ''}),
        'price': forms.NumberInput(attrs={'class': ''}),
        'short_description': forms.TextInput(attrs={'class': ''}),
        'sizes': forms.SelectMultiple(attrs={'class': ''}),
        'category': forms.Select(attrs={'class': ''}),
        'tags': forms.SelectMultiple(attrs={'class':''}),
        'description': forms.Textarea(attrs={'class': ''}),
        # 'image': forms.ClearableFileInput(attrs={'class': ''}),
        'user': forms.Select()
    }
    
    
class ImagePlantForm(forms.ModelForm):
    class Meta:
        model = ImagePlant
        fields = ['image']

    widgets = {
        'image': forms.ClearableFileInput(attrs={'class': ''}),
    }