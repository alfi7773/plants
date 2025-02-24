from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('plant/<int:pk>', views.DetailPlant.as_view(), name='detail_plant'),
    path('blog/<int:pk>', views.DetailBlog.as_view(), name='detail_blog'),
]
