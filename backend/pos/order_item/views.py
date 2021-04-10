from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import OrderItem
from .serializers import OrderItemSerializer


class OrderItemCreateView(CreateAPIView):
    queryset = OrderItem.object.all()
    serializer_class = OrderItemSerializer
