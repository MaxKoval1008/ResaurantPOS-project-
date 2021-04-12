from rest_framework import serializers
from .models import Order_item


class Order_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_item
        fields = '__all__'
