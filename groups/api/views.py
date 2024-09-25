from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from groups.models import Group
from groups.api.serializers import GroupSerializer


class GroupListView(generics.ListAPIView):
    """
    A view for listing all groups in the system.

    Inherits from the generics.ListAPIView to handle GET requests for listing Group model instances.

    Attributes:
        queryset: A queryset of all Group instances in the database.
        serializer_class: The serializer class used for serializing Group instances.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupListCreateView(generics.ListCreateAPIView):
    """
     GroupListCreateView class provides the functionality to list all group objects as well as create a new group object.

     Attributes:
        queryset: A queryset of all group objects.
        serializer_class: The serializer class to be used for validating and deserializing input, and for serializing output.
        permission_classes: Permission classes that determine the access level required to interact with this view.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class GroupUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Class-based view for retrieving, updating, and deleting Group instances.

    Attributes:
        queryset: A QuerySet representing all Group instances in the database.
        serializer_class: The serializer class used to validate and deserialize input,
                          and to serialize output.
        permission_classes: A list of permission classes that determines permissions
                            required to access the view.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
