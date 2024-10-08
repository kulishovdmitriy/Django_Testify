# Generated by Django 4.2 on 2024-08-06 17:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_alter_student_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rating',
            field=models.SmallIntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
