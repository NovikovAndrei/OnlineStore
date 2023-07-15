from rest_framework import serializers
from .models import Cart, Wishlist

class CartSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S')
    updated_at = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S')
    class Meta:
        model = Cart
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    class Meta:
        model = Wishlist
        fields = '__all__'

