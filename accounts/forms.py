from django import forms
from django.core.validators import RegexValidator
from django.forms import NumberInput
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


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
                regex=r'^[a-zA-Z\s]*$',
                message='Firstname must be letters only'),
        ],
        error_messages={
            'required': ''
        }
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]*$',
                message='Lastname must be letters only'),
        ],
        error_messages={
            'required': ''
        }
    )

    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]*$',
                message='Middle name must be letters only'),
        ],
        error_messages={
            'required': ''
        }
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

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'}),
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
                message='Invalid phone number format'),
        ],
        error_messages={
            'required': ''
        }
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
            'username',
            'birth_date',
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(  # This is always 'username'
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'name': 'email',
                'placeholder': 'Email'}
        )
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password',
                'placeholder': 'Password'}
        )
    )
