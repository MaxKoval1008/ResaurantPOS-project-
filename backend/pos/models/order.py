from django.utils.timezone import localtime, localdate
from django.db import models
from .table import Table


class Order(models.Model):
    DISCOUNT_0 = 0
    DISCOUNT_10 = 10
    DISCOUNT_15 = 15
    DISCOUNT_25 = 20
    DISCOUNT_50 = 25
    DISCOUNT = [
        (DISCOUNT_0, 'NO DISCOUNT'),
        (DISCOUNT_10, 'PROMO 10'),
        (DISCOUNT_15, 'PROMO 15'),
        (DISCOUNT_25, 'FAVORITE CLIENT'),
        (DISCOUNT_50, 'PERSONAL')
    ]

    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE)
    start_date = models.DateField(default=localdate, blank=True)
    start_time = models.TimeField(default=localtime, blank=True)
    is_active = models.BooleanField(default=True)
    discount_choice = models.PositiveIntegerField('Discount', choices=DISCOUNT, default=0, blank=True)
    order_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f'Order №{self.pk}'
