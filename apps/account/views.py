from rest_framework import viewsets
from rest_framework import permissions
from account.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    class Meta:
        model = User
        fields = (
            'id',
            'mobile',
            'name',
        )
