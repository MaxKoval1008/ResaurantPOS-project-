from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import Table
from .serializers import TableSerializer


class TableCreateView(CreateAPIView):
    queryset = Table.object.all()
    serializer_class = TableSerializer
