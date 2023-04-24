from django.shortcuts import render, get_object_or_404
from .models import Itinerary

# Create your views here.

def itinerary_list(request):
    itineraries = Itinerary.objects.all()
    context = {
        'itineraries': itineraries
    }
    return render(request, 'itinerary_list.html', context)

def itinerary_detail(request, id):
    itinerary = get_object_or_404(Itinerary, id=id)
    context = {
        'itinerary': itinerary
    }
    return render(request, 'itinerary_detail.html', context)
