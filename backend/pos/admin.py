from django.contrib import admin
from .models.order import Order
from .models.category import Category
from .models.order_item import OrderItem
from .models.product import Product
from .models.table import Table

admin.site.register(Order)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Table)
