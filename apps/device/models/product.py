from django.db import models
from common.models import TimestampMixin
from ..utils import generate_random_string


class Product(TimestampMixin, models.Model):
    name = models.CharField('产品名称', max_length=128)
    version = models.CharField('产品版本', max_length=32)
    product_key = models.CharField('product key', unique=True, max_length=11, editable=False)
    product_secret = models.CharField('product secret', unique=True, max_length=16, editable=False)
    product_desc = models.CharField('产品描述', max_length=128, blank=True)

    def regenerate_secret(self):
        """重新生成secret
        """
        randstr = generate_random_string(16)
        while self.__class__.objects.filter(product_key=randstr).count():
            randstr = generate_random_string(16)
        self.product_secret = randstr
        self.save()

    def save(self, *args, **kwargs):
        # 生成product key
        if not self.product_key:
            randstr = generate_random_string(11)
            while self.__class__.objects.filter(product_key=randstr).count():
                randstr = generate_random_string(11)
            self.product_key = randstr

        # 生成product secret
        if not self.product_secret:
            randstr = generate_random_string(16)
            while self.__class__.objects.filter(product_key=randstr).count():
                randstr = generate_random_string(16)
            self.product_secret = randstr

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'
        db_table = 'product'
