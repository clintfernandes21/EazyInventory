from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import EmployeeRegisterForm, EmployeeLoginForm
from accounts.models import Employees
from django.contrib import messages

def employee_register(request):
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_login')
    else:
        form = EmployeeRegisterForm()
    return render(request, 'accounts/employee_register.html', {'form': form})

def employee_login(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            return redirect('employee_home')
        else:
            messages.error(request, 'Invalid username or password Try again.')
    else:
        form = EmployeeLoginForm()
    return render(request, 'accounts/employee_login.html', {'form': form})
    
def employee_home(request):
    active_user_id = request.session.get('user_id')
    if Employees.objects.get(id=active_user_id).username == "admin":
        return redirect(admin_home)
    else:
        if active_user_id:
            return render(request, 'accounts/employee_home.html')
        else:
            return redirect('employee_login')

def employee_logout(request):
    logout(request)
    return redirect('landing_page')

def admin_home(request):
    active_user_id = request.session.get('user_id')
    if active_user_id:
        return render(request, 'accounts/admin_home.html')
    else:
        return redirect('employee_login')

def admin_logout(request):
    logout(request)
    return redirect('landing_page')