from django.db import models
from django.utils import timezone
from ..product.models import Product


class Order_item(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    count = models.PositiveIntegerField
    total_price = models.DecimalField
    is_ready = models.BooleanField(default=None)

    def __str__(self):
        return f'{self.product.name} {self.count}'