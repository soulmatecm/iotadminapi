from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token, obtain_jwt_token

from .apirouters import router

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', obtain_jwt_token),
    path('token/verify/', verify_jwt_token),
    path('token/refresh/', refresh_jwt_token),

    path('admin/', admin.site.urls),
]
