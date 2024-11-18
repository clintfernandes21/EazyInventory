# assets/models.py
from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=30)
    ASSET_CATEGORY_CHOICES = [
        ('Laptop', 'Laptop'),
        ('Desktop', 'Desktop'),
        ('Server', 'Server'),
        ('Projector', 'Projector'),
        ('CCTV Camera', 'CCTV Camera'),
    ]
    category = models.CharField(max_length=20, choices=ASSET_CATEGORY_CHOICES)
    tag = models.CharField(unique=True, primary_key=True, max_length=20)
    ASSET_BRAND_CHOICES = [
        ('Apple', 'Apple'),
        ('Asus', 'Asus'),
        ('HP', 'HP'),
        ('Lenovo', 'Lenovo'),
        ('Microsoft', 'Microsoft'),
        ('MSI', 'MSI'),
    ]
    brand = models.CharField(max_length=20, choices=ASSET_BRAND_CHOICES)
    purchase_date = models.DateField()
    
    def __str__(self):
        return str(self.name)

class Component(models.Model):
    name = models.CharField(max_length=30)
    COMPONENT_CATEGORY_CHOICES = [
        ('Hard Disk', 'Hard Disk'),
        ('SSD', 'SSD'),
        ('RAM', 'RAM'),
        ('Processor', 'Processor'),
        ('Motherboard', 'Motherboard'),
        ('PSU', 'PSU'),
    ]
    category = models.CharField(max_length=20, choices=COMPONENT_CATEGORY_CHOICES)
    tag = models.CharField(unique=True, primary_key=True, max_length=20)
    COMPONENT_BRAND_CHOICES = [
        ('Cooler Master', 'Cooler Master'),
        ('Crucial', 'Crucial'),
        ('DeepCool', 'DeepCool'),
        ('HP', 'HP'),
        ('Kingston', 'Kingston'),
        ('Samsung', 'Samsung'),
        ('WD', 'WD'),
    ]
    brand = models.CharField(max_length=20, choices=COMPONENT_BRAND_CHOICES)
    purchase_date = models.DateField()
    
    def __str__(self):
        return str(self.name)