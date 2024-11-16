# landing/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('', include('accounts.urls')),
]