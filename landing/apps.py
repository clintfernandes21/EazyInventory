"""landing/apps.py"""
from django.apps import AppConfig


class LandingConfig(AppConfig):
    """Class representing Landing Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landing'
