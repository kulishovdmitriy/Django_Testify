from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from accounts.models import User
from accounts.api.serializers import RegistrationSerializer, AccountSerializer


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AccountView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
