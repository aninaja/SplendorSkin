from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import date


# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=11, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=1000, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=False, blank=False)
    GENDER_CHOICES = [
        ('', '---------'),
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    ]
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
    )
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    ROLE_CHOICES = [
        ('', '---------'),
        ('PATIENT', 'Patient'),
        ('THERAPIST', 'Therapist'),
        ('ADMIN', 'Admin'),
    ]
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
    )

    date_joined = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Available')

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'accounts'
