from django.db import models
from django.utils import timezone


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

    table = models.ForeignKey(to='pos_label.Table', on_delete=models.CASCADE, related_name='table')
    start_time = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    discount_choice = models.CharField(choices=DISCOUNT, default=None, blank=True, null=True, max_length=25)
    total_order_cost = models.DecimalField

    def __str__(self):
        return f'Order №{self.pk}'
