import datetime

from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=64, null=False)
    course = models.CharField(max_length=64, null=True)
    start_date = models.DateField(null=True, default=datetime.date.today)

    def __str__(self):
        return f"{self.name}, {self.course}, {self.start_date}"
