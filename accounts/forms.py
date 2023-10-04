from django import forms
from django.core.validators import RegexValidator
from django.forms import NumberInput
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]*$',
                message='Firstname must be letters only'),
        ]
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]*$',
                message='Lastname must be letters only'),
        ]
    )

    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]*$',
                message='Middle name must be letters only'),
        ]
    )

    gender = forms.ChoiceField(
        choices=CustomUser.GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'})
    )

    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
                message='Invalid phone number format'),
        ]
    )

    birth_date = forms.DateField(
        widget=NumberInput(
            attrs={'type': 'date',
                   'class': 'form-control'},
        )
    )

    class Meta:
        model = CustomUser
        fields = [
            'role',
            'first_name',
            'last_name',
            'middle_name',
            'gender',
            'email',
            'mobile',
            'birth_date',
        ]
