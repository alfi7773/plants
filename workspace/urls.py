from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', views.DeletePlant.as_view(), name='delete'),
    path('main/', views.ListPlant.as_view(), name='work'),
]
