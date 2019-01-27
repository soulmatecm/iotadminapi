from rest_framework import serializers
from ..models import Device
from .product import ProductSerializer
from .group import GroupSerializer


class DeviceSerializer(serializers.ModelSerializer):
    product_detail = ProductSerializer(source='product', read_only=True)
    group_detail = GroupSerializer(source='group', read_only=True)

    class Meta:
        model = Device
        fields = '__all__'
        read_only_fields = ('device_secret',)


class DeviceBulkCreateSerializer(serializers.Serializer):
    add_type = serializers.CharField(label='添加类型')
    add_count = serializers.CharField(label='添加数量')
    device_name_List = serializers.ListSerializer(child=serializers.ListField())

    def create(self, validated_data):
        print(validated_data)
