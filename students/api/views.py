from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from students.api.serializers import StudentSerializer
from students.models import Student


class StudentListView(generics.ListAPIView):
    """
    Generic API view to list all Student records in the database

    Inherits:
        generics.ListAPIView: A generic class-based view for read-only operations

    Attributes:
        queryset: Queryset containing all Student objects in the database
        serializer_class: Serializer class used to serialize the Student objects
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    """
    StudentListCreateView Class

    This view inherits from Django REST framework's ListCreateAPIView.
    It provides a way to list all student objects and create a new student object.

    Attributes:
        queryset: A QuerySet that includes all the Student objects.
        serializer_class: Specifies the serializer to be used; StudentSerializer in this case.
        permission_classes: List of permission classes; IsAuthenticated ensures that only authenticated users can access this view.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class StudentUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
        A view that provides retrieve, update, and delete actions for Student instances.

        This view allows an authenticated user to:
        - Retrieve the details of a specific Student instance by making a GET request.
        - Update a specific Student instance by making a PUT or PATCH request.
        - Delete a specific Student instance by making a DELETE request.

        Attributes:
            queryset: A queryset containing all Student instances.
            serializer_class: The serializer class used to validate and deserialize input, and to serialize output.
            permission_classes: A list containing the IsAuthenticated permission class, which ensures that only authenticated users can access these actions.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
