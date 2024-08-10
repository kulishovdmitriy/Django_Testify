import datetime
import random
import uuid

from django.db import models

from faker import Faker


# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=True)
    birthdate = models.DateField(null=True, default=datetime.date.today)
    subject = models.CharField(max_length=64, null=False)
    years_of_experience = models.IntegerField(null=False)
    uuid = models.UUIDField(null=True, default=uuid.uuid4)

    def full_name_teacher(self):
        return f"{self.first_name} {self.last_name}"

    def age_teacher(self):
        if self.birthdate:
            return datetime.datetime.now().date().year - self.birthdate.year

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
        return (f"{self.full_name_teacher()}, {self.age_teacher()}, {self.subject}, {self.years_of_experience}, "
                f"{self.email}")
