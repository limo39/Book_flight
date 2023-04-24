from django.db import models

# Create your models here.

class Itinerary(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    flights = models.ManyToManyField('flights.Flight')

    def __str__(self):
        return self.name