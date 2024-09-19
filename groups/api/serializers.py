from rest_framework import serializers

from groups.models import Group


class GroupSerializer(serializers.ModelSerializer):
    head = serializers.StringRelatedField()

    class Meta:
        model = Group
        fields = [
            'name',
            'course',
            'start_date',
            'head',
            'classrooms'
        ]
