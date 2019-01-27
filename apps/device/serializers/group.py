from rest_framework import serializers

from common.fields import RecursiveField
from ..models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupRecursiveSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    desc = serializers.CharField(read_only=True)
    create_time = serializers.DateTimeField(read_only=True)
    children = serializers.ListSerializer(source="sub_groups", child=RecursiveField(), read_only=True)

    def to_representation(self, instance):
        """
        为了方便前端三级联动，如果instance没有子节点，则返回的json里面去掉children字段
        """
        ret = super().to_representation(instance)
        if not instance.sub_groups.exists():
            ret.pop('children')
        return ret
