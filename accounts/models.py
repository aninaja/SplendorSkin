from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import os, random
from datetime import date
from django.utils.html import mark_safe


# Create your models here.

class CustomUser(AbstractUser):
    username = None
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
    birth_date = models.DateField(null=False, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    mobile = models.CharField(max_length=100, unique=True, null=False, blank=False)
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

    age = models.PositiveSmallIntegerField()

    def save(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        self.age = age
        super().save()

    date_joined = models.DateTimeField(default=timezone.now())
    deleted_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'mobile'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'accounts'
