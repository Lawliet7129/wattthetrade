# backend/energy_trading/trading/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Example route
]
