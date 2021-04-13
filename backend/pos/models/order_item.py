from django.db import models
from django.utils import timezone
from .product import Product


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_item')
    start_time = models.DateTimeField(default=timezone.now,blank=True)
    product_amount = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=7, decimal_places=2,default=0)
    is_ready = models.BooleanField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.pk}'
