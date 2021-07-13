from .models import Address, UserAccount
from .serializers import (UserCreateSerializer,
                          UserUpdateSerializer, AddressSerializer)
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


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


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def address(request):
    if request.method == 'POST':
        data = {"user_id": request.user.id,
                "user_address": request.data.get('address')}
        data = AddressSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response('CREATED', status=201)

    if request.method == 'GET':
        address = Address.objects.filter(user_id=request.user.id).all()
        data = AddressSerializer(address, many=True).data
        return Response(data, status=200)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def edit_address(request, pk):
    if request.method == 'PUT':
        address = Address.objects.filter(pk=pk).all()
        address.address = request.data.get('address')
        address.save()
        return Response('UPDATED', status=200)

    if request.method == 'DELETE':
        address = Address.objects.filter(pk=pk).all()
        address.delete()
        return Response('DELETED', status=204)
