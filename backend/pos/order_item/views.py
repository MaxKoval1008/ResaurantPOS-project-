from rest_framework import mixins
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, GenericAPIView, ListCreateAPIView
)
from rest_framework.response import Response

from .models import Order_item
from .serializers import CookerSerializer, WaiterSerializer


class Order_itemListView(ListAPIView):
    queryset = Order_item.objects.order_by('-start_time')
    #if waiter:
    #serializer_class = WaiterSerializer
    #elif cooker:
    serializer_class = CookerSerializer


class Order_itemReadyListView(ListAPIView):
    queryset = Order_item.objects.filter(is_ready='True').order_by('-start_time')
    #if waiter:
    #serializer_class = WaiterSerializer
    #elif cooker:
    serializer_class = CookerSerializer


class Order_itemNotReadyListView(ListAPIView):
    queryset = Order_item.objects.filter(is_ready='False').order_by('-start_time')
    #if waiter:
    #serializer_class = WaiterSerializer
    #elif cooker:
    serializer_class = CookerSerializer


class Order_itemUpdateView(mixins.UpdateModelMixin,
                    GenericAPIView):
    queryset = Order_item.objects.all()
    #if waiter:
    #serializer_class = WaiterSerializer
    #elif cooker:
    serializer_class = CookerSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class Order_itemCreateView(CreateAPIView):
    queryset = Order_item.objects.all()
    serializer_class = WaiterSerializer
