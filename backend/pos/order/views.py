from rest_framework import mixins
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, GenericAPIView
)
from .models import Order
from .serializers import WaiterSerializer


class OrderActiveListView(ListAPIView):
    queryset = Order.objects.filter(is_active='True').order_by('table')
    serializer_class = WaiterSerializer


class OrderNotActiveListView(ListAPIView):
    queryset = Order.objects.filter(is_active='False').order_by('start_time')
    serializer_class = WaiterSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = WaiterSerializer


class OrderUpdateView(mixins.UpdateModelMixin,
                    GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = WaiterSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
