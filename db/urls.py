from django.contrib import admin
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


   

urlpatterns = [
    path('', views.search, name = "search"),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('login/', auth_views.LoginView.as_view(template_name='db/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('signup/', views.signup, name='signup'),


]