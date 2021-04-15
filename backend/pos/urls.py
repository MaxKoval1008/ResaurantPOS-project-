from django.urls import path

from .category.views import *
from .order.views import *
from .order_item.views import *
from .product.views import *
from .table.views import *

app_name = 'pos'

urlpatterns = [
    path('cooker/order_item/list/all', Order_itemListView.as_view()),
    path('cooker/order_item/list/ready', Order_itemReadyListView.as_view()),
    path('cooker/order_item/list/not_ready', Order_itemNotReadyListView.as_view()),
    path('cooker/order_item/update/<int:pk>', Order_itemUpdateView.as_view()),
    path('waiter/order_item/create/', Order_itemCreateView.as_view()),
    path('waiter/order_item/list/all', Order_itemListView.as_view()),
    path('waiter/order_item/list/ready', Order_itemReadyListView.as_view()),
    path('waiter/order_item/list/not_ready', Order_itemNotReadyListView.as_view()),
    path('waiter/order_item/update/<int:pk>', Order_itemUpdateView.as_view()),
    path('waiter/order/create', OrderCreateView.as_view()),
    path('waiter/order/list/active', OrderActiveListView.as_view()),
    path('waiter/order/list/not_active', OrderNotActiveListView.as_view()),
    path('waiter/order/update/<int:pk>', OrderUpdateView.as_view()),
    ]
