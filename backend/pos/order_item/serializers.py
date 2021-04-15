from rest_framework import serializers
from .models import Order_item


class CookerSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    order = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order_item
        fields = ['id', 'product', 'order', 'start_time', 'count', 'is_ready']
        read_only_fields = ['id', 'product', 'order', 'start_time', 'count']


class WaiterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_item
        fields = '__all__'
