from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import Table
from .serializers import TableSerializer


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
