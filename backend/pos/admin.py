from django.contrib import admin
from .category.models import Category
from .order.models import Order
from .order_item.models import Order_item
from .product.models import Product
from .table.models import Table


admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(Product)
admin.site.register(Table)
