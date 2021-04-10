from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import Order
from .serializers import OrderSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.object.all()
    serializer_class = OrderSerializer
