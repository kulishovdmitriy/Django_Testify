# Generated by Django 5.1 on 2024-08-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_group_head'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True)),
                ('floor', models.PositiveSmallIntegerField()),
            ],
        ),
    ]