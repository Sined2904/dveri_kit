from django.urls import include, path
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView

from .views import ProductViewSet, ArticleViewSet, RequestForMeasurementViewSet

app_name = 'api'

router = DefaultRouter()

router.register('products', ProductViewSet, basename='products')
router.register('articles', ArticleViewSet, basename='articles')
router.register('request_for_measurement',
                RequestForMeasurementViewSet,
                basename='request_for_measurement'
                )


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(),
         name='swagger-ui'),
    path('v1/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema2'),
         name='redoc'),
]
