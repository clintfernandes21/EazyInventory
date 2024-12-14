"""accounts/urls.py"""
from django.urls import path, include
from .views import employee_register, employee_login, employee_home, employee_logout, admin_home, admin_logout

urlpatterns = [
    path('register/', employee_register, name='employee_register'),
    path('login/', employee_login, name='employee_login'),
    path('employee_home/', employee_home, name='employee_home'),
    path('employee_logout/', employee_logout, name='employee_logout'),
    
    path('admin_home/', admin_home, name='admin_home'),
    path('admin_logout/', admin_logout, name='admin_logout'),
    
    path('', include('assets.urls')),
]
