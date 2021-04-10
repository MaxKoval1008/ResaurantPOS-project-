from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import Category
from .serializers import CategorySerializer


class CategoryCreateView(CreateAPIView):
    queryset = Category.object.all()
    serializer_class = CategorySerializer
