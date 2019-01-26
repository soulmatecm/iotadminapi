from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer, ProductSecretSerializer
from django_filters import rest_framework as filters
from .filters import ProductFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter

    @action(
        methods=['patch'],
        detail=True,
        serializer_class=ProductSecretSerializer,
        url_name='reset_product_secret',
        url_path='secret',
    )
    def reset_product_secret(self, request, pk=None):
        """
        重置product secret
        """
        product = get_object_or_404(Product, pk=pk)
        product.regenerate_secret()
        return Response(data={'detail': '重置product secret成功!'})
