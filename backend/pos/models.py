from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    product = models.CharField(Product, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    count = models.PositiveIntegerField
    total_price = models.DecimalField
    is_ready = models.BooleanField(default=None)

    def __str__(self):
        return f'{self.product.name} {self.count}'


class Table(models.Model):
    is_active = models.BooleanField(default=True)
    comment = models.TimeField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Table №{self.pk}'


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
