from django.db import models
from common.models import TimestampMixin


class Product(TimestampMixin, models.Model):
    name = models.CharField('产品名称', max_length=128)
    version = models.CharField('产品版本', max_length=32)
    product_key = models.CharField('product key', max_length=11)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'
        db_table = 'product'
