from django.db import models
from django.utils import timezone


class Order_item(models.Model):
    product = models.ForeignKey(to='pos_label.Product', on_delete=models.CASCADE, related_name='product')
    order = models.ForeignKey(to='pos_label.Order', on_delete=models.CASCADE, related_name='order')
    start_time = models.DateTimeField(default=timezone.now)
    count = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField
    is_ready = models.BooleanField(default=None)

    def __str__(self):
        if self.count == 1:
            return f'{self.product.name} - {self.count} piece'
        else:
            return f'{self.product.name} - {self.count} pieces'
