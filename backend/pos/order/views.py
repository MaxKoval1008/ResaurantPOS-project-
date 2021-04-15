from rest_framework import mixins
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, GenericAPIView
)
from .models import Order
from .serializers import WaiterSerializer


# class OrderCreateView(CreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class OrderDeleteView(DestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class OrderUpdateView(UpdateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#
#
# class OrderListView(ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


class WaiterListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = WaiterSerializer


class WaiterCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = WaiterSerializer


class WaiterUpdateView(mixins.UpdateModelMixin,
                    GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = WaiterSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
