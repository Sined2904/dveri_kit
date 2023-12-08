from rest_framework import viewsets

from products.models import Product, RelatedProduct
from .serializers import ProductSerializer, RelatedProductSerializer
from .permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для товаров."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class RelatedProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для сопутствующих товаров."""

    queryset = RelatedProduct.objects.all()
    serializer_class = RelatedProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']
