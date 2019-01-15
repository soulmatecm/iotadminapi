from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.admin import AdminSite

from .models import User
from .forms import UserChangeForm, UserCreationForm, UserAuthenticationForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = (
        'mobile', 'create_time', 'is_active', 'is_staff', 'is_superuser',
    )

    fieldsets = (
        (None, {'fields': ('mobile', 'password', 'name')}),
        ('权限', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ('重要日期', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('mobile', 'password1', 'password2'),
        }),
    )
    search_fields = ('mobile',)
    ordering = ('mobile',)


AdminSite.login_form = UserAuthenticationForm
AdminSite.site_header = 'iot后台管理系统'
AdminSite.site_title = 'iot后台管理系统'
