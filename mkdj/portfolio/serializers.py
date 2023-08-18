from rest_framework import serializers
from .models import Portfolio, CartItem, Cart

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = PortSerializer()

    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'