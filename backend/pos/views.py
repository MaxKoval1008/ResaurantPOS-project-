from rest_framework.generics import UpdateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .filters import OrderAdminFilter, OrderWaiterFilter, OrderCookerFilter
from .serializers import CategorySerializer, OrderCookerSerializer, OrderWaiterSerializer, ProductSerializer, \
    TableSerializer, OrderSingleSerializer, OrderItemSingleSerializer, OrderNestedSerializer
from .models.category import Category
from .models.order import Order
from .models.order_item import OrderItem
from .models.product import Product
from .models.table import Table
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from rest_framework.response import Response
from .permissions import IsAdmin, IsWaiter, IsCooker


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
    serializer_class = OrderSingleSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


class OrderSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSingleSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


class OrderItemListCreateView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSingleSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


class OrderItemSingleView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSingleSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class OrderNestedAdminListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderNestedSerializer
    filterset_class = OrderAdminFilter
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]

    def get(self, request, *args, **kwargs):
        order = Order.objects.all()
        filterset = OrderAdminFilter(request.GET, queryset=order)
        if filterset.is_valid():
            order = filterset.qs
        serializer = OrderNestedSerializer(order, many=True)
        total_income = order.aggregate(Sum('order_cost'))['order_cost__sum']
        return Response({'Total income': total_income if total_income else 0, 'Orders': serializer.data})


class OrderNestedWaiterListCreateView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderWaiterSerializer
    filterset_class = OrderWaiterFilter
    permission_classes = [IsAuthenticated & (IsAdmin | IsWaiter)]


class OrderItemCookerListView(ListAPIView):
    queryset = OrderItem.objects.all().order_by('is_ready')
    serializer_class = OrderCookerSerializer
    filterset_class = OrderCookerFilter
    permission_classes = [IsAuthenticated & (IsAdmin | IsCooker)]


class OrderItemCookerUpdateView(UpdateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderCookerSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsCooker)]
