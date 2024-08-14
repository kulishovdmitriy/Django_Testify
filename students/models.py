import random

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from faker import Faker

from groups.models import Group
from teachers.models import Teacher
from core.models import Person

# Create your models here.


class Student(Person):

    rating = models.SmallIntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)

    group = models.ForeignKey(to=Group, null=True, on_delete=models.SET_NULL, related_name='students')

    teacher = models.ForeignKey(to=Teacher, null=True, on_delete=models.SET_NULL, related_name='students')

    @staticmethod
    def generate_students(count):
        faker = Faker()

        for _ in range(count):
            student = Student(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                birthdate=faker.date_between('-30y', '-20y'),
                rating=random.randint(0, 100)
            )
            student.save()

    def __str__(self):
        return f"{super().__str__()}, {self.rating}"
