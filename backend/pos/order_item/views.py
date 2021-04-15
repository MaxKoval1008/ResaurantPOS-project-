from rest_framework import mixins
from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, GenericAPIView, ListCreateAPIView
)
from rest_framework.response import Response

from .models import Order_item
from .serializers import CookerSerializer


# class Order_itemCreateView(CreateAPIView):
#     queryset = Order_item.objects.all()
#     serializer_class = Order_itemSerializer
#
#
# class Order_itemDeleteView(DestroyAPIView):
#     queryset = Order_item.objects.all()
#     serializer_class = Order_itemSerializer
#
#
# class Order_itemUpdateView(UpdateAPIView):
#     queryset = Order_item.objects.all()
#     serializer_class = Order_itemSerializer
#
#
# class Order_itemListView(ListAPIView):
#     queryset = Order_item.objects.all()
#     serializer_class = Order_itemSerializer


class CookerListView(ListAPIView):
    queryset = Order_item.objects.order_by('-start_time')
    serializer_class = CookerSerializer


class CookerReadyListView(ListAPIView):
    queryset = Order_item.objects.filter(is_ready='True').order_by('-start_time')
    serializer_class = CookerSerializer


class CookerNotReadyListView(ListAPIView):
    queryset = Order_item.objects.filter(is_ready='False').order_by('-start_time')
    serializer_class = CookerSerializer


class CookerUpdateView(mixins.UpdateModelMixin,
                    GenericAPIView):
    queryset = Order_item.objects.all()
    serializer_class = CookerSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
