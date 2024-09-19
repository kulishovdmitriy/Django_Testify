from rest_framework import serializers

from students.models import Student
from teachers.api.serializers import TeacherSerializer
from groups.api.serializers import GroupSerializer


class StudentSerializer(serializers.ModelSerializer):
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
