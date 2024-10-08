# Generated by Django 5.1 on 2024-08-12 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_rename_group_id_student_group'),
        ('teachers', '0007_teacher_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_of_students', to='teachers.teacher'),
        ),
    ]
