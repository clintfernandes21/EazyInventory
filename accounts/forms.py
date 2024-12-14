"""accounts/forms.py"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

class EmployeeRegisterForm(UserCreationForm):
    """Class representing Employee Registration Form"""
    first_name = forms.CharField(max_length=30, required=True, label="Firstname", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, label="Lastname", widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=30, required=True, label="Employee ID", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=30, required=True, label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=30, required=True, label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        """Class representing Meta"""
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'member'
        if commit:
            user.save()
        return user

class EmployeeLoginForm(forms.Form):
    """Class representing Employee Login Form"""
    username = forms.CharField(max_length=150, label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
