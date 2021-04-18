from django.db import models
from .product import Product
from .order import Order
from decimal import Decimal
from django.utils import timezone


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    start_date = models.DateField(blank=True,null=True)
    start_time = models.TimeField(blank=True)
    count = models.PositiveIntegerField('Product amount',default=1)
    order_item_cost = models.DecimalField('Position cost',max_digits=7, decimal_places=2, default=0)
    is_ready = models.BooleanField(default=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        product_cost = Product.objects.get(pk=self.product.id).price
        self.order_item_cost = product_cost * self.count
        order = Order.objects.get(pk=self.order.id)
        discount = order.discount_choice

        order.order_cost += self.order_item_cost * Decimal(str(1 - discount / 100))
        order.save()
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} - {self.count}'
