"""accounts/apps.py"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Class representing Accounts Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
