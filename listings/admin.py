from django.contrib import admin
from .models import Vehicle, Listing

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('year', 'make', 'model', 'price', 'condition')
    list_filter = ('make', 'year', 'condition')
    search_fields = ('make', 'model', 'vin')

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'vehicle', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'seller_notes')
