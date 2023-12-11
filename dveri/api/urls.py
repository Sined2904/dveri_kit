from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

app_name = 'api'

router = DefaultRouter()

router.register('products', ProductViewSet, basename='products')
# router.register('relatedproducts', RelatedProductViewSet, basename='related')


urlpatterns = [
    path('v1/', include(router.urls)),
]
