from rest_framework import viewsets
from django_filters import rest_framework as filters

from ..serializers import DeviceSerializer
from ..models import Device
from ..filters import DeviceFilter


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = DeviceFilter
