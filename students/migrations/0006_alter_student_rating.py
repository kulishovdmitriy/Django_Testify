# Generated by Django 4.2 on 2024-08-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_student_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='rating',
            field=models.SmallIntegerField(default=0, max_length=100, null=True),
        ),
    ]
