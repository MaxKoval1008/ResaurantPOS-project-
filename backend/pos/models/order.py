from django.db import models
from django.utils import timezone
from .table import Table
from .order_item import OrderItem


class Order(models.Model):
    DISCOUNT_10 = 10
    DISCOUNT_15 = 15
    DISCOUNT_25 = 25
    DISCOUNT_50 = 50
    DISCOUNT = [
        (DISCOUNT_10, 10),
        (DISCOUNT_15, 15),
        (DISCOUNT_25, 25),
        (DISCOUNT_50, 50)
    ]

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    start_time = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=None)
    discount_choice = models.CharField(choices=DISCOUNT, max_length=2, default=None, blank=True, null=True)
    total_order_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        order_items = OrderItem.objects.filter(order=self.pk)
        self.total_order_cost = 0
        for item in order_items:
            self.total_order_cost = (self.total_order_cost + item.total_price) * Decimal(100 - int(self.discount_choice))
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f'Order №{self.pk}'
