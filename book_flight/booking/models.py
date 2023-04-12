from django.db import models
from django.utils import timezone

# Create your models here.

class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.flight_number} - {self.origin} to {self.destination}"
    
class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    passengers = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.flight}"