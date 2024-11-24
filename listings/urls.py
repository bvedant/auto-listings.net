from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.listing_list, name='listing_list'),
    path('<int:pk>/', views.listing_detail, name='listing_detail'),
    path('sell/', views.vehicle_create, name='vehicle_create'),
    path('sell/<int:vehicle_id>/details/', views.listing_details, name='listing_details'),
] 