"""Defines URL schemes for users."""
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


app_name = 'users'
urlpatterns = [
    # Enable default authorization URL
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'), 

]