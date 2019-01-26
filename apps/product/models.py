from django.db import models
from common.models import TimestampMixin
import random


class Product(TimestampMixin, models.Model):
    name = models.CharField('产品名称', max_length=128)
    version = models.CharField('产品版本', max_length=32)
    product_key = models.CharField('product key', unique=True, max_length=11, editable=False)
    product_secret = models.CharField('product secret', unique=True, max_length=16, editable=False)

    @staticmethod
    def generate_random_string(length):
        raw = ''
        range1 = range(58, 65)  # between 0~9 and A~Z
        range2 = range(91, 97)  # between A~Z and a~z
        i = 0
        while i < length:
            seed = random.randint(48, 122)
            if seed in range1 or seed in range2:
                continue
            raw += chr(seed)
            i += 1
        return raw

    def regenerate_secret(self):
        """重新生成secret
        """
        randstr = self.__class__.generate_random_string(16)
        while self.__class__.objects.filter(product_key=randstr).count():
            randstr = self.__class__.generate_random_string(16)
        self.product_secret = randstr
        self.save()

    def save(self, *args, **kwargs):
        # 生成product key
        if not self.product_key:
            randstr = self.__class__.generate_random_string(11)
            while self.__class__.objects.filter(product_key=randstr).count():
                randstr = self.__class__.generate_random_string(11)
            self.product_key = randstr

        # 生成product secret
        if not self.product_secret:
            randstr = self.__class__.generate_random_string(16)
            while self.__class__.objects.filter(product_key=randstr).count():
                randstr = self.__class__.generate_random_string(16)
            self.product_secret = randstr

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品'
        db_table = 'product'
