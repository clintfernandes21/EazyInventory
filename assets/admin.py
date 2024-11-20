# assets/admin.py
from django.contrib import admin
from .models import Asset, Component, AssetRequest

admin.site.register(Asset)
admin.site.register(Component)
admin.site.register(AssetRequest)