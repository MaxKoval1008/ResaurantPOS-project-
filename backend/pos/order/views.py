from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import Order
from .serializers import OrderSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

