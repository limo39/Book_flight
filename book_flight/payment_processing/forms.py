from django import forms
import stripe

class PaymentForm(forms.Form):
    amount = forms.IntegerField(min_value=1)
    currency = forms.ChoiceField(choices=[('usd', 'USD'), ('eur', 'EUR'), ('ksh', 'KSH')])
    stripe_token = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stripe_token'].initial = self.get_stripe_token()
    
    def get_stripe_token(self):
        return stripe.Token.create().id