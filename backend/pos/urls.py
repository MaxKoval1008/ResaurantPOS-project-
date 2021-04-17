from django.urls import path

from .views import *

app_name = 'pos'


urlpatterns = [
    path('admin/category/create/', CategoryCreateView.as_view()),
    path('admin/category/list/', CategoryListView.as_view()),
    path('admin/category/update/<int:pk>', CategoryUpdateView.as_view()),
    path('admin/category/delete/<int:pk>', CategoryDeleteView.as_view()),
    path('admin/order/create/', OrderCreateView.as_view()),
    path('admin/order/list/active', OrderActiveListView.as_view()),
    path('admin/order/list/not_active', OrderNotActiveListView.as_view()),
    path('admin/order/update/<int:pk>', OrderUpdateView.as_view()),
    path('admin/order/delete/<int:pk>', OrderDeleteView.as_view()),
    path('admin/order_item/create/', OrderItemCreateView.as_view()),
    path('admin/order_item/list/all', OrderItemListView.as_view()),
    path('admin/order_item/list/ready', OrderItemReadyListView.as_view()),
    path('admin/order_item/list/not_ready', OrderItemNotReadyListView.as_view()),
    path('admin/order_item/update/<int:pk>', OrderItemUpdateView.as_view()),
    path('admin/order_item/delete/<int:pk>', OrderItemDeleteView.as_view()),
    path('admin/product/create/', ProductCreateView.as_view()),
    path('admin/product/list/', ProductListView.as_view()),
    path('admin/product/update/<int:pk>', ProductUpdateView.as_view()),
    path('admin/product/delete/<int:pk>', ProductDeleteView.as_view()),
    path('admin/table/create/', TableCreateView.as_view()),
    path('admin/table/list/', TableListView.as_view()),
    path('admin/table/update/<int:pk>', TableUpdateView.as_view()),
    path('admin/table/delete/<int:pk>', TableDeleteView.as_view()),

    path('cooker/order_item/list/all', OrderItemListView.as_view()),
    path('cooker/order_item/list/ready', OrderItemReadyListView.as_view()),
    path('cooker/order_item/list/not_ready', OrderItemNotReadyListView.as_view()),
    path('cooker/order_item/update/<int:pk>', OrderItemUpdateView.as_view()),

    path('waiter/order_item/create/', OrderItemCreateView.as_view()),
    path('waiter/order_item/list/all', OrderItemListView.as_view()),
    path('waiter/order_item/list/ready', OrderItemReadyListView.as_view()),
    path('waiter/order_item/list/not_ready', OrderItemNotReadyListView.as_view()),
    path('waiter/order_item/update/<int:pk>', OrderItemUpdateView.as_view()),
    path('waiter/order/create', OrderCreateView.as_view()),
    path('waiter/order/list/active', OrderActiveListView.as_view()),
    path('waiter/order/list/not_active', OrderNotActiveListView.as_view()),
    path('waiter/order/update/<int:pk>', OrderUpdateView.as_view()),
    ]
