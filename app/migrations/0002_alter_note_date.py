# Generated by Django 4.0.3 on 2022-05-19 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(default=datetime.date(2022, 5, 19)),
        ),
    ]
