import datetime
import random

from django.db import models
from faker import Faker

from groups.models import Group
from core.models import Person

# Create your models here.


class Teacher(Person):

    subject = models.CharField(max_length=64, null=False)
    years_of_experience = models.IntegerField(null=False)

    group = models.ForeignKey(to=Group, null=True, on_delete=models.SET_NULL, related_name='teachers')

    @staticmethod
    def generate_teachers(count):
        faker = Faker()

        for _ in range(count):
            teacher = Teacher(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                birthdate=faker.date_of_birth(),
                email=faker.email(),
                subject=faker.random_element(['Math', 'Science', 'English', 'History', 'Geography', "Programming"]),
                years_of_experience=random.randint(1, 12),
            )
            teacher.save()

    def __str__(self):
        return f"{super().__str__()}, {self.subject}, {self.years_of_experience}"
