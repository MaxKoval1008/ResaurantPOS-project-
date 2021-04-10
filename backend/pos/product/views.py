from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import Product
from .serializers import ProductSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.object.all()
    serializer_class = ProductSerializer
