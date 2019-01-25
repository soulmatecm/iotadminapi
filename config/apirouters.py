from rest_framework import routers
from account.views import UserViewset
from product.views import ProductViewSet

router = routers.DefaultRouter()
router.register('users', UserViewset)
router.register('products', ProductViewSet)
