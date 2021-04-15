from django.urls import path

from .category.views import *
from .order.views import *
from .order_item.views import *
from .product.views import *
from .table.views import *

app_name = 'pos'

urlpatterns = [
    path('cooker/list/all', CookerListView.as_view()),
    path('cooker/list/ready', CookerReadyListView.as_view()),
    path('cooker/list/not_ready', CookerNotReadyListView.as_view()),
    path('cooker/update/<int:pk>', CookerUpdateView.as_view()),
    path('waiter/create', WaiterCreateView.as_view()),
    path('waiter/list', WaiterListView.as_view()),
    path('waiter/update/<int:pk>', WaiterUpdateView.as_view()),
    ]
