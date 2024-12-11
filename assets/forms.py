# assets/forms.py
from django import forms
from .models import Asset, Component, AssetRequest
from accounts.models import Employees

class AddAssetForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=Asset.ASSET_CATEGORY_CHOICES, label="Category", widget=forms.Select(attrs={'class': 'form-control'}))
    tag = forms.CharField(max_length=30, required=True, label="Tag", widget=forms.TextInput(attrs={'class': 'form-control'}))
    brand = forms.ChoiceField(choices=Asset.ASSET_BRAND_CHOICES, label="Brand", widget=forms.Select(attrs={'class': 'form-control'}))
    purchase_date = forms.DateField(required=True, label="Purchase Date", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    class Meta:
        model = Asset
        fields = ['name', 'category', 'tag', 'brand', 'purchase_date']

class AddComponentForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(choices=Component.COMPONENT_CATEGORY_CHOICES, label="Category", widget=forms.Select(attrs={'class': 'form-control'}))
    tag = forms.CharField(max_length=30, required=True, label="Tag", widget=forms.TextInput(attrs={'class': 'form-control'}))
    brand = forms.ChoiceField(choices=Component.COMPONENT_BRAND_CHOICES, label="Brand", widget=forms.Select(attrs={'class': 'form-control'}))
    purchase_date = forms.DateField(required=True, label="Purchase Date", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    
    class Meta:
        model = Component
        fields = ['name', 'category', 'tag', 'brand', 'purchase_date']

class AssetCheckOutForm(forms.ModelForm):
    asset = forms.ModelChoiceField(queryset=Asset.objects.exclude(status__in=["CheckedOut", "UnderService", "Discarded"]), label="Select an Asset", widget=forms.Select(attrs={'class': 'form-control'}))
    employee_username = forms.ModelChoiceField(queryset=Employees.objects.exclude(username__in=["admin", "bang1"]), label="Select an Employee", widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Asset
        fields = ['asset', 'employee_username']

class AssetCheckInForm(forms.ModelForm):
    asset = forms.ModelChoiceField(queryset=Asset.objects.exclude(status__in=["CheckedIn", "UnderService", "Discarded"]), label="Select an Asset", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Asset
        fields = ['asset']

class AssetRequestForm(forms.ModelForm):
    asset = forms.ModelChoiceField(queryset=Asset.objects.exclude(status__in=["CheckedOut", "UnderService", "Discarded"]), label="Select an Asset", widget=forms.Select(attrs={'class': 'form-control'}))
    issue_date = forms.DateField(required=True, label="Issue Date", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    return_date = forms.DateField(required=True, label="Return Date", widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    reason = forms.CharField(max_length=30, required=True, label="Reason for request", widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = AssetRequest
        fields = ['asset', 'issue_date', 'return_date', 'reason']

class UpdateRequestStatus(forms.ModelForm):
    asset = forms.ModelChoiceField(queryset=AssetRequest.objects.all(), label="Select an Asset Request", widget=forms.Select(attrs={'class': 'form-control'}))
    updated_status = forms.ChoiceField(choices=AssetRequest.ASSET_REQUEST_STATUS_CHOICES, label="Update Status To", widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Asset
        fields = ['asset', 'updated_status']