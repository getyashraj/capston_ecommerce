from .models import UserAccount
from .serializers import UserCreateSerializer, UserUpdateSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ListUser(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer


class UpdateUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserAccount.objects.all()
    serializer_class = UserUpdateSerializer
