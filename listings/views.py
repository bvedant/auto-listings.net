from django.shortcuts import render, get_object_or_404
from .models import Listing

def listing_list(request):
    listings = Listing.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def listing_create(request):
    # We'll implement this later with forms
    pass
