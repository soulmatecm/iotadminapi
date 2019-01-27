from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response

from ..serializers import DeviceSerializer, DeviceBulkCreateSerializer
from ..models import Device
from ..filters import DeviceFilter


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DeviceFilter

    @action(
        methods=['post'],
        detail=False,
        url_path='batch',
        serializer_class=DeviceBulkCreateSerializer
    )
    def bulk_create_device(self, request):
        """批量添加设备
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response()
