from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    device_count = serializers.SerializerMethodField()

    def get_device_count(self, instance):
        """获取产品下面的设备数量
        """
        return instance.owned_devices.count()

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'version', 'product_key', 'product_secret', 'product_desc', 'device_count', 'create_time',)
        read_only_fields = ('product_key', 'product_secret',)


class ProductSecretSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_secret',)
