from rest_framework.generics import (
    CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
)
from .models import Category
from .serializers import CategorySerializer


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
