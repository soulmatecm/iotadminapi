from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
from base.models import TimestampMixin

#  手机号码规则校验
#  需要根据最新的各运营商手机号规则编写
MobileValidator = RegexValidator(
    regex=r'^1[345678]\d{9}$',
    message='手机号码不合法',
    code='invalid mobile number',
)


class UserManager(BaseUserManager):
    """
    用户管理器
    """

    def _create_user(self, mobile, password, **extra_fields):
        if not mobile:
            raise ValueError('用户名（手机号码）必须设定')
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile, password, **extra_fields)

    def create_superuser(self, mobile, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(mobile, password, **extra_fields)


class User(TimestampMixin, PermissionsMixin, AbstractBaseUser):
    """
    用户模型
    """

    mobile = models.CharField(
        '电话号码',
        max_length=11,
        unique=True,
        validators=[MobileValidator, ]
    )

    name = models.CharField(
        '姓名',
        max_length=32,
        unique=True,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        '有效',
        default=True,
        help_text='指明用户是否被认为活跃的。以反选代替删除帐号。'
    )

    is_staff = models.BooleanField(
        '职员状态',
        default=False,
        help_text='指明用户是否能登陆admin站点。',
    )

    # 用户名字段指定为手机号
    USERNAME_FIELD = 'mobile'

    objects = UserManager()

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name_plural = '用户'
        verbose_name = '用户'
        db_table = 'user'
