from rest_framework import serializers
from .models.order import Order
from .models.order_item import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('product', 'start_time', 'is_ready')

'''
OrderCreateUpdateSerializer helps to create/update order with one or many order items
TEST VERSION
NOT ALL FIELDS SERIALIZED. Used default values. 

TODO:
add all fields
'''
class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('table','start_time','is_active','order_item',)

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
        instance.save()
        for item in order_items_data:
            order_item = order.pop(0)
            order_item.name = item.get('name', order_item.name)
            order_item.product = item.get('product', order_item.product)
            order_item.start_time = item.get('start_time', order_item.start_time)
            order_item.is_ready = item.get('is_ready', order_item.is_ready)
            order_item.save()
        return instance

