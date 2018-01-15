from rest_framework import generics

from spendtracks.api.core.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
