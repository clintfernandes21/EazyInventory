# landing/views.py
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing/index.html')