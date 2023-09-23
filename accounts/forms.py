from django import forms
from django.core.validators import RegexValidator
from django.forms import NumberInput
from django.forms import ModelForm
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
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

    birth_date = forms.DateField(
        widget=NumberInput(
        attrs={'type': 'date',
               'class': 'form-control'},


    ))

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'})
    )

    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
    )

    age = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^\d{1,2}$',
                message="Age must be number",
            ),
        ]
    )

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'middle_name',
            'birth_date',
            'email',
            'mobile',
            'role',
            'age',
            'user_image',
        ]
