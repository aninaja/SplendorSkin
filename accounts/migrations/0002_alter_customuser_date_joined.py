# Generated by Django 4.2.5 on 2023-10-06 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 1, 3, 45, 27978, tzinfo=datetime.timezone.utc)),
        ),
    ]