# assets/models.py
from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=20)
    ASSET_CATEGORY_CHOICES = [
        ('Laptop', 'Laptop'),
        ('Desktop', 'Desktop'),
        ('Server', 'Server'),
        ('Projector', 'Projector'),
        ('CCTV Camera', 'CCTV Camera'),
    ]
    category = models.CharField(max_length=20, choices=ASSET_CATEGORY_CHOICES)
    tag = models.CharField(max_length=20)
    purchase_date = models.DateField()
    
    def __str__(self):
        return str(self.name)