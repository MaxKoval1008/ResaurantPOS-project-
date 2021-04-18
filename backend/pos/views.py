from rest_framework import mixins
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, GenericAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models.category import Category
from .models.order import Order
from .models.order_item import OrderItem
from .models.product import Product
from .models.table import Table
from .serializers import CategorySerializer, CookerOrderItemSerializer, \
    WaiterOrderItemSerializer, ProductSerializer, TableSerializer, OrderSerializer, OrderItemSerializer, \
    AdminStatisticsSerializer


# AdminStatisticsSerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderActiveListView(ListAPIView):
    queryset = Order.objects.filter(is_active='True').order_by('table')
    serializer_class = OrderSerializer


class OrderNotActiveListView(ListAPIView):
    queryset = Order.objects.filter(is_active='False').order_by('start_time')
    serializer_class = OrderSerializer


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemListView(ListAPIView):
    queryset = OrderItem.objects.order_by('-start_time')
    # if waiter:
    # serializer_class = WaiterSerializer
    # elif cooker:
    serializer_class = CookerOrderItemSerializer


class OrderItemReadyListView(ListAPIView):
    queryset = OrderItem.objects.filter(is_ready='True').order_by('-start_time')
    # if waiter:
    # serializer_class = WaiterOrderItemSerializer
    # elif cooker:
    serializer_class = CookerOrderItemSerializer


class OrderItemNotReadyListView(ListAPIView):
    queryset = OrderItem.objects.filter(is_ready='False').order_by('-start_time')
    # if waiter:
    # serializer_class = WaiterOrderItemSerializer
    # elif cooker:
    serializer_class = CookerOrderItemSerializer


class OrderItemUpdateView(UpdateAPIView):
    queryset = OrderItem.objects.all()
    # if waiter:
    # serializer_class = WaiterOrderItemSerializer
    # elif cooker:
    serializer_class = CookerOrderItemSerializer


class OrderItemCreateView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = WaiterOrderItemSerializer


class OrderItemDeleteView(DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class TableCreateView(CreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDeleteView(DestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableUpdateView(UpdateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableListView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class AdminStatisticsView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return_order_cost = {"sum": str(sum([lambda items: int(items['amount'])])), "objects": serializer.data}
        return Response(return_order_cost)
