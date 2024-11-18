# assets/urls.py
from django.urls import path, include
from .views import add_asset, view_asset, add_component, view_component

urlpatterns = [
    path('add_asset/', add_asset, name='add_asset'),
    path('view_asset/', view_asset, name='view_asset'),
    path('add_component/', add_component, name='add_component'),
    path('view_component/', view_component, name='view_component'),
]