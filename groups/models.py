import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class ClassRoom(models.Model):
    """

        Django model class representing a classroom.

        Attributes:
        name: The name of the classroom. It's a character field with a maximum length of 32 characters and allows null values.
        floor: The floor on which the classroom is located. It's a positive small integer field with a value between 1 and 4.

        Methods:
        __str__: Returns a string representation of the classroom including its name and floor.
    """

    name = models.CharField(max_length=32, null=True)
    floor = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __str__(self):
        return f"{self.name}, floor {self.floor}"


class Group(models.Model):
    """
    Represents a Group entity with fields and relationships in a Django application.

    Class Group inherits from models.Model.

    Attributes:
        name (models.CharField): The name of the group. Maximum length is 64 characters and cannot be null.
        course (models.CharField): Name of the course associated with the group. Maximum length is 64 characters and can be null.
        start_date (models.DateField): The starting date of the group. It can be null and defaults to the current date.
        head (models.OneToOneField): A one-to-one relationship to the 'students.Student' model. It can be null and uses the SET_NULL option on deletion. Uses 'head_of_group' as the related name.
        classrooms (models.ManyToManyField): A many-to-many relationship to the ClassRoom model. Uses 'groups' as the related name.

    Methods:
        __str__:
            Returns a string representation of the group, containing name, course, start_date, and head.
    """

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
