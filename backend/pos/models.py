from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank= True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    product = models.CharField(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField(default=timezone.now)
    count = models.PositiveIntegerField
    total_price = models.DecimalField
    is_ready = models.BooleanField(default=None)

    def __str__(self):
        return self.name


class Order(models.Model):
    TABLE_1 = '1'
    TABLE_2 = '2'
    TABLE_3 = '3'
    TABLE_4 = '4'
    TABLE_5 = '5'
    TABLE_6 = '6'
    TABLE_7 = '7'
    TABLE_8 = '8'
    TABLES = [
        (TABLE_1, 'Table 1'),
        (TABLE_2, 'Table 2'),
        (TABLE_3, 'Table 3'),
        (TABLE_4, 'Table 4'),
        (TABLE_5, 'Table 5'),
        (TABLE_6, 'Table 6'),
        (TABLE_7, 'Table 7'),
        (TABLE_8, 'Table 8')
    ]
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

    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    table_choice = models.CharField(choices=TABLES, default=None)
    start_time = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=None)
    discount_choice = models.CharField(choices=DISCOUNT, default=None, blank=True, null=True)
    total_order_cost = models.DecimalField

    def __str__(self):
        return f'Order №{self.pk}'
