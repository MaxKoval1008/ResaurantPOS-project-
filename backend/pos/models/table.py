from django.db import models

class Table(models.Model):
    is_active = models.BooleanField(default=True)
    comment = models.TimeField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Table №{self.pk}'