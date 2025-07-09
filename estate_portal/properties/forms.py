from django import forms

from .models import DealRequest


class DealRequestForm(forms.ModelForm):
    class Meta:
        model = DealRequest
        exclude = ('seeker', 'property', 'status')
