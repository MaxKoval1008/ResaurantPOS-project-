from rest_framework.generics import CreateAPIView

from .serializers import *

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

