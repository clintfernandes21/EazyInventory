"""assets/models.py"""
from django.db import models
from accounts.models import Employees

class Asset(models.Model):
    """Class representing Assets"""
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
        ('Dell', 'Dell'),
        ('HP', 'HP'),
        ('Lenovo', 'Lenovo'),
        ('Microsoft', 'Microsoft'),
        ('MSI', 'MSI'),
    ]
    brand = models.CharField(max_length=20, choices=ASSET_BRAND_CHOICES)
    purchase_date = models.DateField()
    ASSET_STATUS_CHOICES = [
        ('CheckedIn', 'CheckedIn'),
        ('CheckedOut', 'CheckedOut'),
        ('UnderService', 'UnderService'),
        ('Discarded', 'Discarded')
    ]
    status = models.CharField(max_length=20, choices=ASSET_STATUS_CHOICES, null=True, blank=True, default="CheckedIn")
    assigned_to = models.ForeignKey(Employees, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Component(models.Model):
    """Class representing Components"""
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

class AssetRequest(models.Model):
    """Class representing Asset Requests"""
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    reason = models.CharField(max_length=200)
    request_date = models.DateTimeField(auto_now_add=True, null=True)
    ASSET_REQUEST_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined')
    ]
    status = models.CharField(max_length=20, choices=ASSET_REQUEST_STATUS_CHOICES, null=True, blank=True, default="Pending")
    
    def __str__(self):
        return str(self.asset)
