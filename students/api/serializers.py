from rest_framework import serializers

from students.models import Student
from teachers.api.serializers import TeacherSerializer
from groups.api.serializers import GroupSerializer


class StudentSerializer(serializers.ModelSerializer):
    """
    A serializer class for the Student model that includes nested serialization for group and teacher.

    Fields:
    - first_name: The first name of the student.
    - last_name: The last name of the student.
    - email: The email address of the student.
    - birthdate: The birth date of the student.
    - rating: The rating of the student.
    - group: Nested GroupSerializer that represents the group a student belongs to.
    - teacher: Nested TeacherSerializer that represents the teacher assigned to the student.

    Meta class:
    - model: Specifies the model class that is being serialized.
    - fields: Specifies the fields that should be included in the serialized output.
    """

    group = GroupSerializer()
    teacher = TeacherSerializer()

    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'birthdate',
            'rating',
            'group',
            'teacher',
        ]
