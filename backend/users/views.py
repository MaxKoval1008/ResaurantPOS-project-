from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrReadOnly, CanGetListUser
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import UserSerializer, UserUpdateSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('is_active')
    serializer_class = UserSerializer
    #permission_classes = [CanGetListUser, IsAdminUser]
    filterset_fields = ['email', 'phone_number']


class UserRetrieveDestroyView(RetrieveAPIView, DestroyAPIView):
    lookup_field = 'email'
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAdminUser, IsOwnerOrReadOnly]


class UserUpdateView(UpdateAPIView):
    lookup_field = 'email'
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    #permission_classes = [IsOwnerOrReadOnly]

