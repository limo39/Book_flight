from django.shortcuts import render, redirect
from .models import Booking, Flight
from .forms import BookingForm

def book_flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passenger_form = PassengerForm(request.POST or None)

    if request.method == 'POST':
        if passenger_form.is_valid():
            passenger = passenger_form.save(commit=False)
            passenger.flight = flight
            passenger.save()
            return redirect('flight_detail', flight_id=flight.id)

    context = {
        'flight': flight,
        'passenger_form': passenger_form,
    }

    return render(request, 'book_flight.html', context)


def home(request):
    return render(request, 'home.html')

def flight(request):
    return render(request, 'flight.html')
