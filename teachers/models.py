import random

from django.db import models
from faker import Faker

from groups.models import Group
from core.models import Person

# Create your models here.


class Teacher(Person):
    """
    class Teacher(Person):

        A model representing a teacher, inheriting from the Person model.

        Attributes:
            subject: A CharField representing the subject the teacher specializes in.
            years_of_experience: An IntegerField indicating the number of years the teacher has been teaching.
            group: A ForeignKey linking to the Group model, indicating the group the teacher is associated with.

        Methods:
            generate_teachers(count):
                Generates a specified number of teacher instances with random data and saves them to the database.

            __str__(): Returns a string representation of the teacher instance, including the subject and years
             of experience.
    """

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
