from rest_framework import viewsets
from rest_framework import permissions
from account.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(
        methods=['get'],
        detail=False,
        url_path='me',
        url_name='me',
        permission_classes=(permissions.IsAuthenticated,)
    )
    def get_my_info(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    class Meta:
        model = User
        fields = (
            'id',
            'mobile',
            'name',
        )
