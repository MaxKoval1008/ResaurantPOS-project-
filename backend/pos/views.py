from rest_framework.generics import UpdateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .filters import AdminOrderFilter, WaiterOrderFilter, CoockerOrderFilter
from .serializers import CategorySerializer, CookerOrderSerializer, WaiterOrderSerializer, ProductSerializer, \
    TableSerializer, SingleOrderSerializer, SingleOrderItemSerializer, OrderNestedSerializer
from .models.category import Category
from .models.order import Order
from .models.order_item import OrderItem
from .models.product import Product
from .models.table import Table
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from rest_framework.response import Response
from .permissions import IsAdmin, IsWaiter, IsCoocker


class TableListCreateView(ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class TableSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class CategorySingleView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class ProductSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class OrderListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = SingleOrderSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


class OrderSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = SingleOrderSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


class OrderItemListCreateView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = SingleOrderItemSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


class OrderItemSingleView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = SingleOrderItemSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class OrderNestedAdminListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderNestedSerializer
    filterset_class = AdminOrderFilter
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]

    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        filterset = AdminOrderFilter(request.GET, queryset=order)
        if filterset.is_valid():
            order = filterset.qs
        serializer = OrderNestedSerializer(order, many=True)
        total_income = order.aggregate(Sum('order_cost'))['order_cost__sum']
        return Response({'Total income': total_income if total_income else 0, 'Orders': serializer.data})


class WaiterOrderNestedListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = WaiterOrderSerializer
    filterset_class = WaiterOrderFilter
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


class CookerOrderItemListView(ListAPIView):
    queryset = OrderItem.objects.all().order_by('is_ready')
    serializer_class = CookerOrderSerializer
    filterset_class = CoockerOrderFilter
    permission_classes = [IsAuthenticated & (IsAdmin | IsCoocker)]


class CookerOrderItemUpdateView(UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = CookerOrderSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsCoocker)]
