from rest_framework import serializers
from .models import Order


class WaiterSerializer(serializers.ModelSerializer):
    table = serializers.StringRelatedField

    class Meta:
        model = Order
        fields = '__all__'
