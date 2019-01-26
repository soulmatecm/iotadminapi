from django.contrib import admin
from .models import Device, Product


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'device_secret', 'status',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'version', 'product_key', 'product_secret',)
