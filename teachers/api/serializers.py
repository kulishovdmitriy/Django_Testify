from rest_framework import serializers

from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'email',
            'birthdate',
            'subject',
            'years_of_experience'
        ]
