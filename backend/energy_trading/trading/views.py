# backend/energy_trading/trading/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Energy Trading Platform!")

