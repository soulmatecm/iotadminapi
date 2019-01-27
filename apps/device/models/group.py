from django.db import models
from common.models import TimestampMixin


class Group(TimestampMixin, models.Model):
    name = models.CharField('分组名称', max_length=32, unique=True)
    parent = models.ForeignKey(
        'self',
        verbose_name='上级分组',
        null=True,
        blank=True,
        related_name='sub_groups',
        on_delete=models.CASCADE
    )
    desc = models.CharField('分组描述', max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分组'
        verbose_name_plural = '分组'
        db_table = 'device_group'
