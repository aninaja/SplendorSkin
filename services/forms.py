from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm

from .models import Service, Treatment, TreatmentArea, PriceType


class ServiceForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]*$',
                message='Service name must be letters only'),
        ]
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}))

    class Meta:
        model = Service
        fields = ['name', 'description']


class TreatmentForm(ModelForm):
    service_id = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'}))

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]*$',
                message='Treatment name must be letters only'),
        ]
    )

    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}))

    area_id = forms.ModelChoiceField(
        queryset=TreatmentArea.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'}))

    type_id = forms.ModelChoiceField(
        queryset=PriceType.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'}))

    price = forms.DecimalField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
    )

    class Meta:
        model = Treatment
        fields = [
            'service_id',
            'name',
            'description',
            'area_id',
            'type_id',
            'price',
        ]


class AreaForm(ModelForm):
    area = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]*$',
                message='Treatment area must be letters only'),
        ]
    )

    class Meta:
        model = TreatmentArea
        fields = ['area']


class TypeForm(ModelForm):
    type = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]*$',
                message='Price type must be letters only'),
        ]
    )

    class Meta:
        model = PriceType
        fields = ['type']

