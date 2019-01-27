class CreateListMixin:
    """允许批量创建资源
    """
    # 重写get_serializer（）方法
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)
