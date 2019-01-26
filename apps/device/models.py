from django.db import models
from common.models import TimestampMixin
import random


class Device(TimestampMixin, models.Model):
    name = models.CharField('产品名称', max_length=32, unique=True, null=True, blank=True)
    device_secret = models.CharField('device secret', max_length=16, unique=True, editable=False)

    @staticmethod
    def generate_random_string(length):
        """生成随机字符串
        """
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

    def save(self, *args, **kwargs):
        """创建时，为设备生成secret
        """
        if not self.device_secret:
            randstr = self.__class__.generate_random_string(16)
            while self.__class__.objects.filter(device_secret=randstr).count():
                randstr = self.__class__.generate_random_string(16)
            self.device_secret = randstr
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备'
        db_table = 'device'
