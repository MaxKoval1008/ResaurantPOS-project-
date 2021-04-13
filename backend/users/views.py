from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

'''
TEST VERSION OF VIEWS
'''


class UserAllView(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes =

    # def post(self, request,*args,**kwargs):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(data=serializer.data)


