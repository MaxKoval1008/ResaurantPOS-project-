from django.urls import  include, path
from .views import OrderView, OrderItemView


from .views import OrderView, OrderItemView

app_name = 'users'

urlpatterns = [

    path('order/', OrderView.as_view()),
    path('order_item', OrderItemView.as_view())



]