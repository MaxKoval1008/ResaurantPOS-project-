from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import Category, Product, OrderItem, Table, Order
from .serializers import (
    CategorySerializer, ProductSerializer, OrderItemSerializer, TableSerializer, OrderSerializer
)


class CategoryCreateView(CreateAPIView):
    queryset = Category.object.all()
    serializer_class = CategorySerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.object.all()
    serializer_class = ProductSerializer


class OrderItemCreateView(CreateAPIView):
    queryset = OrderItem.object.all()
    serializer_class = OrderItemSerializer


class TableCreateView(CreateAPIView):
    queryset = Table.object.all()
    serializer_class = TableSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.object.all()
    serializer_class = OrderSerializer

