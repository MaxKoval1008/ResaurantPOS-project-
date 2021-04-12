from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField

    def __str__(self):
        return self.name