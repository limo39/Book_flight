from django.shortcuts import render, redirect
from .models import Booking, Flight, Airplane, Payment
from .forms import BookingForm, AirplaneForm, PaymentForm
from django.contrib import messages
from django.conf import settings
import stripe

def book_flight(request, flight_id=None):
    if flight_id is None:
        return redirect('select_flight')

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

def add_airplane(request):
    if request.method == 'POST':
        form = AirplaneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('airplanes')
    else:
        form = AirplaneForm()

    return render(request, 'add_airplane.html', {'form': form})

def select_flight(request):
    flights = Flight.objects.all()
    return render(request, 'select_flight.html', {'flights': flights})

def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    context = {'flight': flight}
    return render(request, 'flight_detail.html', context)

stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Retrieve the amount and currency from the form data
            amount = int(form.cleaned_data['amount'])
            currency = form.cleaned_data['currency']
            # Create a new payment object
            payment = Payment(amount=amount, currency=currency, user=request.user)
            payment.save()
            try:
                # Use Stripe API to create a new charge
                charge = stripe.Charge.create(
                    amount=amount * 100,
                    currency=currency,
                    description='Flight booking payment',
                    source=form.cleaned_data['stripe_token']
                )
                # Update the payment status to completed
                payment.status = Payment.COMPLETED
                payment.save()
                messages.success(request, 'Payment completed successfully.')
                return redirect('booking_confirmation')
            except stripe.error.CardError as e:
                # Handle card errors
                payment.status = Payment.FAILED
                payment.save()
                messages.error(request, str(e))
            except stripe.error.StripeError:
                # Handle other Stripe errors
                payment.status = Payment.FAILED
                payment.save()
                messages.error(request, 'An error occurred while processing your payment.')
        else:
            form = PaymentForm()
        context = {
            'form': form,
        }
        return render(request, 'payment.html', context)

