from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import Order_item
from .serializers import Order_itemSerializer


class Order_itemCreateView(CreateAPIView):
    queryset = Order_item.objects.all()
    serializer_class = Order_itemSerializer


class Order_itemDeleteView(DestroyAPIView):
    queryset = Order_item.objects.all()
    serializer_class = Order_itemSerializer


class Order_itemUpdateView(UpdateAPIView):
    queryset = Order_item.objects.all()
    serializer_class = Order_itemSerializer


class Order_itemListView(ListAPIView):
    queryset = Order_item.objects.all()
    serializer_class = Order_itemSerializer
