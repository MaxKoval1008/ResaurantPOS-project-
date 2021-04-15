from rest_framework import serializers
from .models import Order


class WaiterSerializer(serializers.ModelSerializer):
    table = serializers.StringRelatedField
    order_item = serializers.StringRelatedField(many=True)

    class Meta:
        model = Order
        fields = '__all__'
