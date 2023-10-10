from django import forms
from django.forms import ModelForm, NumberInput

from services.models import Treatment
from .models import Appointment


class BookingForm(forms.ModelForm):

    day = forms.DateField(
        widget=NumberInput(
            attrs={'type': 'date',
                   'class': 'form-control'},
        )
    )

    time = forms.ChoiceField(
        choices=Appointment.TIME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    treatment = forms.ModelChoiceField(
        queryset=Treatment.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'}))

    class Meta:
        model = Appointment
        fields = [
            'day',
            'time',
            'treatment',
        ]