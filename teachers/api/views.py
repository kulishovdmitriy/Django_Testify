from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from teachers.api.serializers import TeacherSerializer
from teachers.models import Teacher


class TeacherListView(generics.ListAPIView):
    """
    A view that returns a list of all Teacher instances.

    Inherits from:
        generics.ListAPIView

    Attributes:
        queryset (QuerySet): The complete set of Teacher objects from the database.
        serializer_class (Serializer): The serializer class used to convert Teacher objects to JSON format.
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherListCreateView(generics.ListCreateAPIView):
    """
    TeacherListCreateView
    Class-based view for listing and creating Teacher instances.

    Attributes:
    queryset : QuerySet
        The set of Teacher objects to be queried from the database.

    serializer_class : Serializer
        The serializer class used for validating and deserializing input,
        and for serializing output.

    permission_classes : list
        Contains the permission classes that this view requires.
        Here, it ensures that the user is authenticated.
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]


class TeacherUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
         Class for retrieving, updating, and deleting Teacher instances via API.

         Inherits:
             generics.RetrieveUpdateDestroyAPIView: Provides retrieve, update, and destroy actions.

         Attributes:
             queryset: Queryset containing all Teacher objects.
             serializer_class: Serializer class used for validating and deserializing input, and for serializing output.
             permission_classes: List of permission classes that need to be fulfilled to access the API.
    """

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]
