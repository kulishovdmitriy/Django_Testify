import uuid
import datetime

from django.db import models

# Create your models here.


class Person(models.Model):
    """
    class Person(models.Model):
    Abstract base class for a person

    first_name: str
        The first name of the person, required with a maximum length of 64 characters.
    last_name: str
        The last name of the person, required with a maximum length of 64 characters.
    email: str
        Optional email address of the person, with a maximum length of 64 characters.
    birthdate: datetime.date
        Optional birthdate of the person, defaults to the current date if not provided.
    uuid: uuid.UUID
        Optional unique identifier for the person, defaults to a randomly generated UUID.

    def full_name_person(self):
        Returns the full name of the person, composed of the first name and the last name.

    def age_person(self):
        Calculates and returns the age of the person based on the birthdate.
        If birthdate is not provided, returns None.

    def __str__(self):
        Returns a string representation of the person object, including the id, full name, age, and email.
    """

    class Meta:
        abstract = True

    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=64, null=True)
    birthdate = models.DateField(null=True, default=datetime.date.today)
    uuid = models.UUIDField(null=True, default=uuid.uuid4)

    def full_name_person(self):
        return f"{self.first_name} {self.last_name}"

    def age_person(self):
        if self.birthdate:
            return datetime.datetime.now().date().year - self.birthdate.year
        return None

    def __str__(self):
        return f"{self.id}, {self.full_name_person()}, {self.age_person()}, {self.email}"
