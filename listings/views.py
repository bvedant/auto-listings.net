from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, Vehicle
from .forms import VehicleForm, ListingDetailsForm

def listing_list(request):
    listings = Listing.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = Vehicle.objects.create(**form.cleaned_data)
            return redirect('listings:listing_details', vehicle_id=vehicle.id)
    else:
        form = VehicleForm()
    
    return render(request, 'listings/vehicle_form.html', {'form': form})

def listing_details(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    
    if request.method == 'POST':
        form = ListingDetailsForm(request.POST)
        if form.is_valid():
            listing = Listing.objects.create(
                vehicle=vehicle,
                **form.cleaned_data
            )
            return redirect('listings:listing_detail', pk=listing.pk)
    else:
        form = ListingDetailsForm()
    
    return render(request, 'listings/listing_details_form.html', {
        'form': form,
        'vehicle': vehicle
    })
