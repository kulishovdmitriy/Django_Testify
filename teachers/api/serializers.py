from rest_framework import serializers

from teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    """

        Serializer class for the Teacher model.

        This class serializes the data for the Teacher model, converting it to and from JSON format.
        It includes the following fields from the Teacher model:

        - first_name: The first name of the teacher.
        - last_name: The last name of the teacher.
        - email: The email address of the teacher.
        - birthdate: The birthdate of the teacher.
        - subject: The subject taught by the teacher.
        - years_of_experience: The number of years the teacher has been teaching.

        This allows easy transformation of Teacher instances into JSON and vice versa for API responses.
    """

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
