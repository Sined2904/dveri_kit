from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail

from products.models import (Product, Article, RequestForMeasurement,
                             RequestForCallback)
from .serializers import (ProductSerializer, ArticleSerializer,
                          MinMaxPriceSerializer,
                          RequestForMeasurementSerializer,
                          RequestForCallbackSerializer)

from .permissions import IsAdminOrReadOnly
from .filters import ProductFilter
from dveri import settings


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
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=['GET',])
    def min_max_price(self, request):
        return Response(MinMaxPriceSerializer(self.queryset).data,
                        status=status.HTTP_200_OK)


class ArticleViewSet(viewsets.ModelViewSet):
    """Вьюсет для статей."""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']


class RequestForMeasurementViewSet(viewsets.ModelViewSet):
    """Вьюсет для запроса на замер."""

    queryset = RequestForMeasurement.objects.all()
    serializer_class = RequestForMeasurementSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    def create(self, request, *args, **kwargs):
        message = (f"Фамилия имя: {request.data['name_surname']} \n"
                   f"Телефон: {request.data['telefone']}\n"
                   f"Адрес: {request.data['address']}\n"
                   f"Что замерять: {request.data['content']}"
                   )
        send_mail(f"Новая заявка на замер от {request.data['name_surname']}!",
                  message, settings.EMAIL_HOST_USER,
                  ['den2904@yandex.ru'])
        return super().create(request, *args, **kwargs)


class RequestForCallbackViewSet(viewsets.ModelViewSet):
    """Вьюсет для заявки на обратный звонок."""

    queryset = RequestForCallback.objects.all()
    serializer_class = RequestForCallbackSerializer
    permission_classes = (AllowAny,)
    pagination_class = None

    def create(self, request, *args, **kwargs):
        message = (f"Фамилия имя: {request.data['name_surname']}\n"
                   f"Телефон: {request.data['telefone']}\n"
                   )
        send_mail(f"Запрос звонка от {request.data['name_surname']}!",
                  message, settings.EMAIL_HOST_USER,
                  ['den2904@yandex.ru'])
        return super().create(request, *args, **kwargs)


'''
class RelatedProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для сопутствующих товаров."""

    queryset = RelatedProduct.objects.all()
    serializer_class = RelatedProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None
    http_method_names = ['get']
'''
