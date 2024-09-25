import random

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from faker import Faker

from groups.models import Group
from teachers.models import Teacher
from core.models import Person

# Create your models here.


class Student(Person):
    """
    class Student(Person):

    Represents a student entity that inherits from the Person class.

    Attributes:
    rating (int): The rating of the student, which is a small integer between 0 and 100, defaulting to 0.
    group (ForeignKey): A foreign key relation to the Group model. If the related group is deleted, the group will be set to null.
    teacher (ForeignKey): A foreign key relation to the Teacher model. If the related teacher is deleted, the teacher will be set to null.

    Methods:
    generate_students(count):
        Static method that generates a specified number of student instances with random data using the Faker library and saves them to the database.
    __str__():
        Returns a string representation of the student, including their inherited attributes from the Person class and their rating.
    """

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
