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

    def str(self):
        return f'{self.pk}'

    def save(self, *args, **kwargs):
        product_cost = Product.objects.get(pk=self.product.id).price

        self.total_price = product_cost * self.product_amount
        order = Order.objects.get(pk=self.order.id)
        discount = Order.objects.get(pk=self.order.id).discount_choice
        order.total_order_cost += self.total_price * Decimal(str(1-discount/100))
        order.save()
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        if self.count == 1:
            return f'{self.product.name} - {self.count} piece'
        else:
            return f'{self.product.name} - {self.count} pieces'
