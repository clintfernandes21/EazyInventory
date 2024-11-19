# assets/urls.py
from django.urls import path, include
from .views import add_asset, view_asset, checkout_asset, checkin_asset, add_component, view_component
from .views import employee_view_asset

urlpatterns = [
    path('add_asset/', add_asset, name='add_asset'),
    path('view_asset/', view_asset, name='view_asset'),
    path('checkout_asset/', checkout_asset, name='checkout_asset'),
    path('checkin_asset/', checkin_asset, name='checkin_asset'),
    
    path('add_component/', add_component, name='add_component'),
    path('view_component/', view_component, name='view_component'),
    
    path('employee_view_asset/', employee_view_asset, name='employee_view_asset'),
]