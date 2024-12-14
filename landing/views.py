"""landing/views.py"""
from django.shortcuts import render
# from django.contrib.auth import login, authenticate, logout, get_user_model
# from accounts.forms import EmployeeRegisterForm, EmployeeLoginForm
# from django.contrib import messages

def landing_page(request):
    """Landing Page"""
    return render(request, 'landing/index.html')
