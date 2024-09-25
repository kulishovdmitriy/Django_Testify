from rest_framework import serializers

from groups.models import Group


class GroupSerializer(serializers.ModelSerializer):
    """
    GroupSerializer is a serializer for the Group model.
    It maps data representations between JSON and Group model instances.

    Attributes:
    head: A string representation of the head associated with the group.
    Meta: Contains metadata for the serializer.

    Meta:
    model: The model that is being serialized, in this case, Group.
    fields: Specifies the fields to be included in the serialization output which are 'name', 'course', 'start_date', 'head', and 'classrooms'.
    """

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
