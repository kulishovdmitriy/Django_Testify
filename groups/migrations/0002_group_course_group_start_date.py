# Generated by Django 4.2 on 2024-08-10 18:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='start_date',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
