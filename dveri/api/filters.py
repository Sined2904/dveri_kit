from django_filters import FilterSet, NumberFilter
from django_filters import rest_framework as filters
from products.models import Product, SizeDoor


class ProductFilter(FilterSet):
    """Фильтр для товаров."""

    size = filters.ModelMultipleChoiceFilter(
        field_name='SizeDoor__slug',
        to_field_name='slug',
        queryset=SizeDoor.objects.all(),
    )
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte',)

    class Meta:
        model = Product
        fields = ['type', 'category', 'name',
                  'for_sale', 'old_price', 'for_order',
                  'hit_sale', 'size']
