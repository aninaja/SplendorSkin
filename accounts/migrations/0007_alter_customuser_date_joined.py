# Generated by Django 4.2.5 on 2023-10-07 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_customuser_birth_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 7, 12, 42, 7, 260112, tzinfo=datetime.timezone.utc)),
        ),
    ]