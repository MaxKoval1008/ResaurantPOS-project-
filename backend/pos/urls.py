from django.urls import path

from .views import CategoryListCreateView, CategorySingleView, TableSingleView, TableListCreateView, \
    ProductListCreateView, ProductSingleView, OrderListCreateView, OrderSingleView, OrderItemListCreateView, \
    OrderItemSingleView, OrderNestedAdminListCreateView, OrderNestedWaiterListCreateView, OrderItemCookerListView, \
    OrderItemCookerUpdateView

urlpatterns = [
    path('category', CategoryListCreateView.as_view()),
    path('category/<int:pk>', CategorySingleView.as_view()),
    path('table', TableListCreateView.as_view()),
    path('table/<int:pk>', TableSingleView.as_view()),
    path('product', ProductListCreateView.as_view()),
    path('product/<int:pk>', ProductSingleView.as_view()),
    path('order', OrderListCreateView.as_view()),
    path('order/<int:pk>', OrderSingleView.as_view()),
    path('order_item', OrderItemListCreateView.as_view()),
    path('order_item/<int:pk>', OrderItemSingleView.as_view()),
    path('order_admin', OrderNestedAdminListCreateView.as_view()),
    path('order_waiter', OrderNestedWaiterListCreateView.as_view()),
    path('order_cooker', OrderItemCookerListView.as_view()),
    path('order_cooker/<int:pk>', OrderItemCookerUpdateView.as_view())
    ]
