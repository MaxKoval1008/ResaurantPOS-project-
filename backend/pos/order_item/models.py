from django.db import models
from django.utils import timezone
from ..product.models import Product


class Order_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    start_time = models.DateTimeField(default=timezone.now)
    count = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField
    is_ready = models.BooleanField(default=None)

    def __str__(self):
        if self.count == 1:
            return f'{self.product.name} - {self.count} piece'
        else:
            return f'{self.product.name} - {self.count} pieces'
