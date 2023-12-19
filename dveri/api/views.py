from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from products.models import Product, Article
from .serializers import ProductSerializer, ArticleSerializer
from .permissions import IsAdminOrReadOnly
from .filters import ProductFilter


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для товаров."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]
    ordering_fields = ('price',)
    search_fields = ('name', 'description')
    filterset_class = ProductFilter


class ArticleViewSet(viewsets.ModelViewSet):
    """Вьюсет для товаров."""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


'''
class RelatedProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для сопутствующих товаров."""

    queryset = RelatedProduct.objects.all()
    serializer_class = RelatedProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']
'''
