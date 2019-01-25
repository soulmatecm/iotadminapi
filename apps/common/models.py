from django.db import models


class TimestampMixin(models.Model):
    create_time = models.DateTimeField(
        '创建时间',
        auto_now_add=True
    )

    update_time = models.DateTimeField(
        '修改时间',
        auto_now=True
    )

    class Meta:
        abstract = True


