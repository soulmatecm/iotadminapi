from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response

from ..serializers import GroupSerializer, GroupRecursiveSerializer
from ..models import Group
from ..filters import GroupFilter


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = GroupFilter

    @action(
        methods=['get'],
        detail=False,
        url_path='tree',
        serializer_class=GroupRecursiveSerializer
    )
    def get_group_tree(self, request):
        groups = Group.objects.filter(parent__isnull=True)
        serializer = self.get_serializer(groups, many=True)
        return Response(serializer.data)
