from rest_framework import routers

from account.views import UserViewset


router = routers.DefaultRouter()
router.register('users', UserViewset)

