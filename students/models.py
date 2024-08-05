import datetime

from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    birthdate = models.DateTimeField(null=True, default=datetime.datetime.today)
