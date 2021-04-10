from django.db import models
from django.utils import timezone
from ..order_item.models import OrderItem
from ..table.models import Table


class Order(models.Model):
    DISCOUNT_10 = '10%'
    DISCOUNT_15 = '15%'
    DISCOUNT_25 = '25%'
    DISCOUNT_50 = '50%'
    DISCOUNT = [
        (DISCOUNT_10, 'PROMO 10'),
        (DISCOUNT_15, 'PROMO 15'),
        (DISCOUNT_25, 'FAVORITE CLIENT'),
        (DISCOUNT_50, 'PERSONAL')
    ]

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=None)
    discount_choice = models.CharField(choices=DISCOUNT, default=None, blank=True, null=True)
    total_order_cost = models.DecimalField

    def __str__(self):
        return f'Order №{self.pk}'
