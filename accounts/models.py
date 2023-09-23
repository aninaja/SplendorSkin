from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import os, random
from datetime import datetime
from django.utils.html import mark_safe


# Create your models here.
def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'profile_pic/{year}-{month}-{imageid}-{basename}-{randomstring}-{ext}'.format(imageid=instance.pk,
                                                                                         basename=basefilename,
                                                                                         randomstring=randomstr,
                                                                                         ext=file_extension,
                                                                                         year=_now.strftime('%Y'),
                                                                                         month=_now.strftime('%m'),
                                                                                         day=_now.strftime('%d'))


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=1000, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    mobile = models.PositiveBigIntegerField(unique=True, null=False, blank=False)


    PATIENT = 'patient'
    THERAPIST = 'therapist'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        ('', '-----'),
        (PATIENT, 'Patient'),
        (THERAPIST, 'Therapist'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=PATIENT,
    )

    age = models.PositiveSmallIntegerField(null=False, blank=False)
    date_joined = models.DateTimeField(default=timezone.now())
    deleted_at = models.DateTimeField(null=True, blank=True)
    user_image = models.ImageField(upload_to=image_path, default='profile_pic/image.jpg')

    def image_tag(self):
        return mark_safe('<img src="/users/media/%s" width="50", heigth="50"/>' % (self.user_image))

    USERNAME_FIELD = 'mobile'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'accounts'
