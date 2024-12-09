from rest_framework import serializers
from .models import Flower, Customer, Order

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    flower = FlowerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
