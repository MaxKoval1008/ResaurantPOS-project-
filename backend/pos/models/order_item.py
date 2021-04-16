from django.db import models


class OrderItem(models.Model):
    product = models.ForeignKey(to='pos_label.Product', on_delete=models.CASCADE, related_name='product')
    order = models.ForeignKey(to='pos_label.Order', on_delete=models.CASCADE, related_name='order_item')
    start_time = models.DateTimeField(default=timezone.now, blank=True)
    count = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    is_ready = models.BooleanField(default=None)

    def __str__(self):
        if self.count == 1:
            return f'{self.product.name} - {self.count} piece'
        else:
            return f'{self.product.name} - {self.count} pieces'
