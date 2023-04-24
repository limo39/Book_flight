from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm
from .models import Payment
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
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