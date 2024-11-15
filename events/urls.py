from django.urls import path
from . import views
from .views import *
from .views import admin_login

urlpatterns = [
    path('', views.landing, name='landing'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-register/', views.admin_register, name='admin-register'),
    path('admin-login/', views.admin_login, name='admin-login'),
]
