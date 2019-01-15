from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import User


class UserAuthenticationForm(AuthenticationForm):
    """超级管理员才能访问admin站点
    """

    def confirm_login_allowed(self, user):
        if not user.is_active or not (user.is_staff or user.is_superuser):
            raise forms.ValidationError(
                message="您无权限访问此页面",
                code='无权限',
            )


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("两次密码不匹配")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"{}\">this form</a>."
        ),
    )

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # help_text为 '...但是可以通过这个<a href="{}">表单</a>修改密码'
        # 此处将这个help_text格式化，变成'...但是可以通过这个<a href='../password/'>表单</a>修改密码'
        # 来指向实际的改变用户密码的url
        password = self.fields.get('password')
        if password:
            print(password.help_text)
            password.help_text = password.help_text.format('../password/')

        user_permissions = self.fields.get('user_permissions')
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
