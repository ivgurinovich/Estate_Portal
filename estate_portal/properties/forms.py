from django import forms

from estate_portal.properties.models import DealRequest


class DealRequestForm(forms.ModelForm):
    class Meta:
        model = DealRequest
        exclude = ('seeker', 'property', 'status')

