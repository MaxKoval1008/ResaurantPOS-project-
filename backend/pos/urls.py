from django.urls import path

from .category.views import *
from .order.views import *
from .order_item.views import *
from .product.views import *
from .table.views import *

app_name = 'pos'

urlpatterns = [
    path('category/create', CategoryCreateView.as_view()),
    path('category/delete', CategoryDeleteView.as_view()),
    path('category/update', CategoryUpdateView.as_view()),
    path('category/list', CategoryListView.as_view()),
    path('order/create', OrderCreateView.as_view()),
    path('order/delete', OrderCreateView.as_view()),
    path('order/update', OrderCreateView.as_view()),
    path('order/list', OrderCreateView.as_view()),
    path('order_item/create', Order_itemCreateView.as_view()),
    path('order_item/delete', Order_itemDeleteView.as_view()),
    path('order_item/update', Order_itemUpdateView.as_view()),
    path('order_item/list', Order_itemListView.as_view()),
    path('product/create', ProductCreateView.as_view()),
    path('product/delete', ProductDeleteView.as_view()),
    path('product/update', ProductUpdateView.as_view()),
    path('product/list', ProductListView.as_view()),
    path('table/create', TableCreateView.as_view()),
    path('table/delete', TableDeleteView.as_view()),
    path('table/update', TableUpdateView.as_view()),
    path('table/list', TableListView.as_view()),
    ]
