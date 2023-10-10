from datetime import datetime
from django.db import models
from django.utils import timezone
from services.models import Treatment


# Create your models here.
class Appointment(models.Model):
    day = models.DateField(null=True, blank=True)
    TIME_CHOICES = [
        ("------", "------"),
        ("10 AM", "10 AM"),
        ("11 AM", "11 AM"),
        ("12 PM", "12 PM"),
        ("1 PM", "1 PM"),
        ("2 PM", "2 PM"),
        ("3 PM", "3 PM"),
        ("4 PM", "4 PM"),
        ("5 PM", "5 PM"),
        ("6 PM", "6 PM"),
        ("7 PM", "7 PM"),
        ("8 PM", "8 PM"),
        ("9 PM", "9 PM"),
    ]
    time = models.CharField(max_length=10, choices=TIME_CHOICES)
    treatment = models.ForeignKey(Treatment, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.day} {self.time}"

    class Meta:
        db_table = 'appointments'
