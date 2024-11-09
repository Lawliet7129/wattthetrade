# backend/energy_trading/trading/views.py
from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Or another template you have


