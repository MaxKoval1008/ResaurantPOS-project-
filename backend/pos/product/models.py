from django.db import models
from ..category.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    price = models.DecimalField

    def __str__(self):
        return self.name
