from django.shortcuts import render
from .models import Flight

# Create your views here.

def search_flights(request):
    if request.method == 'POST':
        origin = request.POST['origin']
        destination = request.POST['destination']
        departure_date = request.POST['departure_date']
        flights = Flight.objects.filter(origin=origin, destination=destination, departure_date=departure_date)
        return render(request,'search_results.html', {'flights': flights})
    return render(request, 'search_form.html')