from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/category', blank=True, null=True)


    def __str__(self):
        return self.name
