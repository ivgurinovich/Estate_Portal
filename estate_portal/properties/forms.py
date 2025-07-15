from django import forms

from .models import DealRequest, Property


class DealRequestForm(forms.ModelForm):
    class Meta:
        model = DealRequest
        exclude = ('seeker', 'property', 'status')


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ('owner',)
