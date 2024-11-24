from django import forms

class VehicleForm(forms.Form):
    make = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    year = forms.IntegerField()
    mileage = forms.IntegerField()
    price = forms.DecimalField(max_digits=10, decimal_places=0)
    condition = forms.CharField(max_length=50)
    vin = forms.CharField(max_length=17, label="VIN")

class ListingDetailsForm(forms.Form):
    title = forms.CharField(max_length=200)
    seller_notes = forms.CharField(widget=forms.Textarea, required=False)
    