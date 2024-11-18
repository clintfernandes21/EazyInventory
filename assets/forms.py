# assets/forms.py
from django import forms
from .models import Asset, Component

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