import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class ClassRoom(models.Model):
    name = models.CharField(max_length=32, null=True)
    floor = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __str__(self):
        return f"{self.name}, floor {self.floor}"


class Group(models.Model):
    name = models.CharField(max_length=64, null=False)
    course = models.CharField(max_length=64, null=True)
    start_date = models.DateField(null=True, default=datetime.date.today)

    head = models.OneToOneField(
        to='students.Student',
        null=True,
        on_delete=models.SET_NULL,
        related_name='head_of_group'
    )

    classrooms = models.ManyToManyField(
        to=ClassRoom,
        related_name='groups'
    )

    def __str__(self):
        return f"{self.name}, {self.course}, {self.start_date}, {self.head}"
