from django.urls import path
from . import views


urlpatterns = [
    path('plant/<int:pk>', views.DetailPlant.as_view(), name='detail_plant'),
    path('blog/<int:pk>', views.DetailBlog.as_view(), name='detail_blog'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add_to_cart/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove_from_cart/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('catologue/', views.Catologue.as_view(), name='catologue'),
    path('blogs/', views.AllBlogs.as_view(), name='blogs'),
    path('', views.HomePageView.as_view(), name='home'),
]
