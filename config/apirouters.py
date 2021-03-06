from rest_framework import routers
from user.views import UserViewset
from device.views import DeviceViewSet, ProductViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register('users', UserViewset)
router.register('products', ProductViewSet)
router.register('devices', DeviceViewSet)
router.register('groups', GroupViewSet)
