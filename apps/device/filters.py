from django_filters import rest_framework as filters
from .models import Device, Product, Group


class DeviceFilter(filters.FilterSet):
    class Meta:
        model = Device
        fields = {
            'name': ['icontains']
        }


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains']
        }


class GroupFilter(filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'name': ['icontains']
        }
