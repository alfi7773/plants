from django.urls import path
from . import views


urlpatterns = [
    path('plant/<int:pk>', views.DetailPlant.as_view(), name='detail_plant'),
    path('plants/<int:pk>', views.Reviews.as_view(), name='review'),
    path('blog/<int:pk>', views.DetailBlog.as_view(), name='detail_blog'),
    # path('plant/<int:pk>/rate/', views.AddRating.as_view(), name='add_rating'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add_to_cart/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove_from_cart/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('catologue/', views.Catologue.as_view(), name='catologue'),
    path('blogs/', views.AllBlogs.as_view(), name='blogs'),
    path('plants/', views.NewArrivals.as_view(), name='arrivals'),
    path('plant-login/', views.ForLogin.as_view(), name='log'),
    path('order/create/', views.CreateOrderView.as_view(), name='create_order'),
    path('order/<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('', views.HomePageView.as_view(), name='home'),
]
