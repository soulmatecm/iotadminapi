from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('product_key', 'product_secret',)


class ProductSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_secret',)
