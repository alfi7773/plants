import django_filters
from django import forms
from .models import *

# class PlantFilter(django_filters.FilterSet):
    
#     name = django_filters.CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'placeholder': 'Search by name'}))
#     category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Categories', empty_label="Select a category")
#     sizes = django_filters.ModelChoiceFilter(queryset=Size.objects.all(), label='Size', widget=forms.CheckboxSelectMultiple)
#     old_price_min = django_filters.NumberFilter(field_name='old_price', lookup_expr='gte', label='Min Old Price')
#     old_price_max = django_filters.NumberFilter(field_name='old_price', lookup_expr='lte', label='Max Old Price')
    
    


class PlantFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'placeholder': 'Search by name'})
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label='Categories',
        empty_label="Select a category",
    )
    sizes = django_filters.ModelChoiceFilter(
        queryset=Size.objects.all(),
        label='Size',
        # widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    old_price_min = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte', label='Min Old Price'
    )
    old_price_max = django_filters.NumberFilter(
        field_name='price', lookup_expr='lte', label='Max Old Price'
    )
