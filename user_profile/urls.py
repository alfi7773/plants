from django.urls import path
from .views import ProfileUser, RegionListView, SignUpView, Login, CustomLogoutView
from plant import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileUser.as_view(), name='profile'),
    path("get_regions/", RegionListView.as_view(), name="regions"),
    path('', views.HomePageView.as_view(), name='home'),
]
