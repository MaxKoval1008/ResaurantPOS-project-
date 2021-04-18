from rest_framework import serializers
from .models.category import Category
from .models.order import Order
from .models.order_item import OrderItem
from .models.product import Product
from .models.table import Table
from datetime import datetime


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(default=datetime.now().time, format='%H:%M:%S')

    class Meta:
        model = OrderItem
        fields = ('product', 'start_date', 'start_time', 'is_ready')
        read_only_fields = ['is_ready']


class OrderNestedSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)
    discount_choice = serializers.ChoiceField(choices=[0, 10, 15, 20, 25])
    start_time = serializers.TimeField(default=datetime.now().time, format='%H:%M:%S')

    class Meta:
        model = Order
        fields = ('id', 'table', 'start_date', 'start_time', 'is_active', 'order_item', 'discount_choice')
        read_only_fields = ['id', 'order_cost']

    def create(self, validated_data):
        order_items = validated_data.pop('order_item')
        order = Order.objects.create(**validated_data)
        for item in order_items:
            OrderItem.objects.create(order=order, **item)

        return order

    def update(self, instance, validated_data):
        order_items_data = validated_data.pop('order_item')
        order = instance.order_item.all()
        order = list(order)
        instance.table = validated_data.get('table', instance.table)
        instance.start_time = validated_data.get('start_time', instance.start_time)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.discount_choice = validated_data.get('discount_choice', instance.discount_choice)
        instance.save()
        for item in order_items_data:
            order_item = order.pop(0)
            order_item.name = item.get('name', order_item.name)
            order_item.product = item.get('product', order_item.product)
            order_item.start_time = item.get('start_time', order_item.start_time)
            order_item.is_ready = item.get('is_ready', order_item.is_ready)
            order_item.save()
        return instance


class SingleOrderSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(default=datetime.now().time, format='%H:%M:%S')

    class Meta:
        model = Order
        fields = '__all__'


class SingleOrderItemSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(default=datetime.now().time, format='%H:%M:%S')

    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ['is_ready']

class CookerOrderSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'count', 'start_time', 'is_ready',)
        read_only_fields = ('id', 'order', 'product', 'count', 'start_time')


class WaiterOrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_item.is_ready', 'order_item.order_item_cost', 'order_cost']
