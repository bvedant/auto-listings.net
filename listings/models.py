from django.db import models


class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    condition = models.CharField(max_length=50)
    vin = models.CharField(max_length=17)
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Listing(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    seller_notes = models.TextField(blank=True)
    
    def __str__(self):
        return self.title
