from rest_framework.generics import CreateAPIView,UpdateAPIView
from rest_framework.response import Response
from .models.order_item import OrderItem
from .models.order import Order
from .serializers import OrderCreateUpdateSerializer, OrderItemSerializer

'''
TEST VERSION OF VIEWS FOR ORDER AND ORDER ITEM
'''

class OrderView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateUpdateSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(request.data,headers=headers)

class OrderItemView(CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = 'order'