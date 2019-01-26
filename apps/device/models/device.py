from django.db import models
from common.models import TimestampMixin
import random


class Device(TimestampMixin, models.Model):
    DEVICE_STATUS_CHOICES = (
        (1, '未激活'),
        (2, '离线'),
        (3, '在线'),
    )
    name = models.CharField('设备名称', max_length=32, unique=True, null=True, blank=True,
                            help_text='设备名可以为空，如果为空，系统将颁发全局唯一标识符作为设备名')
    device_secret = models.CharField('device secret', max_length=16, unique=True, editable=False)
    product = models.ForeignKey(
        'device.Product',
        verbose_name='所属产品',
        on_delete=models.PROTECT
    )
    status = models.PositiveSmallIntegerField('设备状态', choices=DEVICE_STATUS_CHOICES, default=1)
    last_login = models.DateTimeField('最后上线时间', editable=False, blank=True, null=True)

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

        if not self.name:
            randstr = self.__class__.generate_random_string(11)
            while self.__class__.objects.filter(name=randstr).count():
                randstr = self.__class__.generate_random_string(11)
            self.name = randstr

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备'
        db_table = 'device'
