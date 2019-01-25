from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django_filters import rest_framework as filters
from .filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ProductFilter
