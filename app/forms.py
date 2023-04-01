from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
	passenger_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

class Meta:
    model = Booking
    fields = ['passenger_name', 'passenger_email', 'num_passengers']
    labels = {
        'passenger_name': 'Passenger Name',
        'passenger_email': 'Passenger Email',
        'num_passengers': 'Number of Passengers',
    }

