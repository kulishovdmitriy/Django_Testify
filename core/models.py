import uuid
import datetime

from django.db import models

# Create your models here.


class Person(models.Model):
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
