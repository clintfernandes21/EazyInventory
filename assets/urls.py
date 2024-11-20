# assets/urls.py
from django.urls import path, include
from .views import admin_add_asset, admin_view_asset, admin_checkout_asset, admin_checkin_asset, add_component, view_component, admin_view_request_asset
from .views import employee_view_asset, employee_request_asset, employee_view_request_asset

urlpatterns = [
    path('admin_add_asset/', admin_add_asset, name='admin_add_asset'),
    path('admin_view_asset/', admin_view_asset, name='admin_view_asset'),
    path('admin_checkout_asset/', admin_checkout_asset, name='admin_checkout_asset'),
    path('admin_checkin_asset/', admin_checkin_asset, name='admin_checkin_asset'),
    path('admin_view_request_asset/', admin_view_request_asset, name='admin_view_request_asset'),
    
    path('add_component/', add_component, name='add_component'),
    path('view_component/', view_component, name='view_component'),
    
    path('employee_view_asset/', employee_view_asset, name='employee_view_asset'),
    path('employee_request_asset/', employee_request_asset, name='employee_request_asset'),
    path('employee_view_request_asset/', employee_view_request_asset, name='employee_view_request_asset'),
]