from django.db import models

class Booking(models.Model):
    passenger_name = models.CharField(max_length=255)
    passenger_email = models.EmailField()
    num_passengers = models.PositiveIntegerField()
    flight_date = models.DateField()
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Flight(models.Model):
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)