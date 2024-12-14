"""assets/views.py"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Asset, Component, AssetRequest
from .forms import AddAssetForm, AddComponentForm, AssetCheckOutForm, AssetCheckInForm, AssetRequestForm, UpdateRequestStatus

def admin_add_asset(request):
    """Admin Add Asset"""
    active_user_id = request.session.get('user_id')
    if active_user_id:
        if request.method == 'POST':
            form = AddAssetForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "New asset has been added.")
                return redirect('admin_add_asset')
        else:
            form = AddAssetForm()
        return render(request, 'assets/admin_add_asset.html', {'form': form})
    else:
        return redirect('employee_login')

def admin_view_asset(request):
    """Admin View Asset"""
    active_user_id = request.session.get('user_id')
    all_assets = Asset.objects.all()
    context = {
        'all_assets': all_assets
    }
    if active_user_id:
        return render(request, 'assets/admin_view_asset.html', {'context': context})
    else:
        return redirect('employee_login')

def add_component(request):
    """Admin Add Component"""
    active_user_id = request.session.get('user_id')
    if active_user_id:
        if request.method == 'POST':
            form = AddComponentForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "New component has been added.")
                return redirect('add_component')
        else:
            form = AddComponentForm()
        return render(request, 'assets/add_component.html', {'form': form})
    else:
        return redirect('employee_login')

def view_component(request):
    """Admin View Component"""
    active_user_id = request.session.get('user_id')
    all_components = Component.objects.all()
    context = {
        'all_components': all_components
    }
    if active_user_id:
        return render(request, 'assets/view_component.html', {'context': context})
    else:
        return redirect('employee_login')

def admin_checkout_asset(request):
    """Admin Checkout Asset"""
    active_user_id = request.session.get('user_id')
    if active_user_id:
        if request.method == 'POST':
            form = AssetCheckOutForm(request.POST)
            if form.is_valid():
                asset = form.cleaned_data['asset']
                employee_username = form.cleaned_data['employee_username']
                asset = Asset.objects.get(name=asset)
                asset.status = "CheckedOut"
                asset.save(update_fields=['status'])
                asset.assigned_to = employee_username
                asset.save(update_fields=['assigned_to'])
                
                messages.success(request, "Item checked out successfully.")
                return redirect('admin_checkout_asset')
        else:
            form = AssetCheckOutForm()
        return render(request, 'assets/admin_checkout_asset.html', {'form': form})
    else:
        return redirect('employee_login')

def admin_checkin_asset(request):
    """Admin Checkin Asset"""
    active_user_id = request.session.get('user_id')
    if active_user_id:
        if request.method == 'POST':
            form = AssetCheckInForm(request.POST)
            if form.is_valid():
                asset = form.cleaned_data['asset']
                asset = Asset.objects.get(name=asset)
                asset.status = "CheckedIn"
                asset.save(update_fields=['status'])
                asset.assigned_to = None
                asset.save(update_fields=['assigned_to'])
                
                messages.success(request, "Item checked in successfully.")
                return redirect('admin_checkin_asset')
        else:
            form = AssetCheckInForm()
        return render(request, 'assets/admin_checkin_asset.html', {'form': form})
    else:
        return redirect('employee_login')

def employee_view_asset(request):
    """Employee View Asset"""
    active_user_id = request.session.get('user_id')
    all_assets = Asset.objects.filter(assigned_to=active_user_id)
    context = {
        'all_assets': all_assets
    }
    if active_user_id:
        return render(request, 'assets/employee_view_asset.html', {'context': context})
    else:
        return redirect('employee_login')

def employee_request_asset(request):
    """Employee Request Asset"""
    active_user_id = request.session.get('user_id')
    if active_user_id:
        if request.method == 'POST':
            form = AssetRequestForm(request.POST)
            if form.is_valid():
                asset_request = form.save(commit=False)
                asset_request.employee_id = active_user_id
                asset_request.save()
                messages.success(request, "Asset request has been submitted.")
                return redirect('employee_request_asset')
        else:
            form = AssetRequestForm()
        return render(request, 'assets/employee_request_asset.html', {'form': form})
    else:
        return redirect('employee_login')

def employee_view_request_asset(request):
    """Employee View Requested Assets"""
    active_user_id = request.session.get('user_id')
    all_requests = AssetRequest.objects.filter(employee_id=active_user_id)
    context = {
        'all_requests': all_requests
    }
    if active_user_id:
        return render(request, 'assets/employee_view_request_asset.html', {'context': context})
    else:
        return redirect('employee_login')

def admin_view_request_asset(request):
    """Admin View Requested Assets"""
    active_user_id = request.session.get('user_id')
    all_requests = AssetRequest.objects.all()
    context = {
        'all_requests': all_requests
    }
    if active_user_id:
        return render(request, 'assets/admin_view_request_asset.html', {'context': context})
    else:
        return redirect('employee_login')

def admin_update_request_status(request):
    """Admin Update Requested Assets"""
    active_user_id = request.session.get('user_id')
    if active_user_id:
        if request.method == 'POST':
            form = UpdateRequestStatus(request.POST)
            if form.is_valid():
                asset = form.cleaned_data['asset']
                updated_status = form.cleaned_data['updated_status']
                asset = Asset.objects.get(name=asset)
                asset = asset.tag
                asset = AssetRequest.objects.get(asset=asset)
                asset.status = updated_status
                asset.save(update_fields=['status'])
                messages.success(request, f"Asset Request change to {updated_status}")
                return redirect('admin_update_request_status')
        else:
            form = UpdateRequestStatus()
        return render(request, 'assets/admin_update_request_status.html', {'form': form})
    else:
        return redirect('employee_login')
