# assets/urls.py
from django.urls import path, include
from .views import add_asset, view_asset

urlpatterns = [
    path('add_asset/', add_asset, name='add_asset'),
    path('view_asset/', view_asset, name='view_asset'),
]