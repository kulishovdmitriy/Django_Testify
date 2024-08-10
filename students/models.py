import datetime
import random
import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from faker import Faker

from groups.models import Group

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=True)
    birthdate = models.DateField(null=True, default=datetime.date.today)
    rating = models.SmallIntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    uuid = models.UUIDField(null=True, default=uuid.uuid4)

    group = models.ForeignKey(to=Group, null=True, on_delete=models.SET_NULL, related_name='students')

    def full_name_student(self):
        return f"{self.first_name} {self.last_name}"

    def age_student(self):
        if self.birthdate:
            return datetime.datetime.now().date().year - self.birthdate.year
        return None

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
        return f"{self.id}, {self.full_name_student()}, {self.age_student()}, {self.rating}, {self.email}"
