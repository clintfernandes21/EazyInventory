# assets/views.py
from django.shortcuts import render, redirect
from .models import Asset, Component
from .forms import AddAssetForm, AddComponentForm
from django.contrib import messages

def add_asset(request):
    active_user_id = request.session.get('user_id')
    if active_user_id:
        if request.method == 'POST':
            form = AddAssetForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f"New asset has been added.")
                return redirect('add_asset')
        else:
            form = AddAssetForm()
        return render(request, 'assets/add_asset.html', {'form': form})
    else:
        return redirect('employee_login')

def view_asset(request):
    active_user_id = request.session.get('user_id')
    all_assets = Asset.objects.all()
    context = {
        'all_assets': all_assets
    }
    if active_user_id:
        return render(request, 'assets/view_asset.html', {'context': context})
    else:
        return redirect('employee_login')

def add_component(request):
    active_user_id = request.session.get('user_id')
    if active_user_id:
        if request.method == 'POST':
            form = AddComponentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f"New component has been added.")
                return redirect('add_component')
        else:
            form = AddComponentForm()
        return render(request, 'assets/add_component.html', {'form': form})
    else:
        return redirect('employee_login')

def view_component(request):
    active_user_id = request.session.get('user_id')
    all_components = Component.objects.all()
    context = {
        'all_components': all_components
    }
    if active_user_id:
        return render(request, 'assets/view_component.html', {'context': context})
    else:
        return redirect('employee_login')