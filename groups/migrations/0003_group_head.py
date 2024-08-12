# Generated by Django 5.1 on 2024-08-11 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_course_group_start_date'),
        ('students', '0010_rename_group_id_student_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='head',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='head_of_group', to='students.student'),
        ),
    ]