from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Booking
from .forms import BookingForm

# Create your views here.

def flight_detail(request, id):
    flight = get_object_or_404(Flight, id=id)
    form = BookingForm()
    context = {
        'flight': flight,
        'form': form
    }
    return render(request, 'flight_detail.html', context)

def book_flight(request, id):
    flight = get_object_or_404(Flight, id=id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            book_flight = flight
            booking.save()
            return redirect('booking_confirm', id=booking.id)
        else:
            form = BookingForm()
            context = {
                'flight': flight,
                'form': form
            }
            return render(request, 'book_flight.html', context)