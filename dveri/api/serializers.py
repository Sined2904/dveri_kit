from rest_framework import serializers
from django.db.models import Max, Min

from products.models import (Product, SizeDoor, Article, RequestForMeasurement,
                             ProductAlbum, ProductAlbumColor,
                             RequestForCallback)


class ProductAlbumSerializer(serializers.ModelSerializer):
    """Сериализатор альбома товара."""

    image = serializers.ImageField()

    class Meta:
        model = ProductAlbum
        fields = ['name', 'image',]


class ProductAlbumColorSerializer(serializers.ModelSerializer):
    """Сериализатор альбома цветов товара."""

    image = serializers.ImageField()

    class Meta:
        model = ProductAlbumColor
        fields = ['name', 'image']


'''
class RelatedProductSerializer(serializers.ModelSerializer):
    """Сериализатор сопутствующего товара."""

    class Meta:
        model = RelatedProduct
        fields = ['id', 'name', 'price', 'image', 'description']
'''


class SizeDoorSerializer(serializers.ModelSerializer):
    """Сериализатор альбома товара."""

    class Meta:
        model = SizeDoor
        fields = ['size',]


class SubproductSerializer(serializers.ModelSerializer):
    """Сериализатор сопутствующих товаров."""

    productalbum = serializers.SerializerMethodField()

    def get_productalbum(self, obj):
        productalbum = obj.album_product
        serializer = ProductAlbumSerializer(productalbum, many=True)
        return serializer.data

    class Meta:
        model = Product
        fields = ['id', 'type', 'category', 'name', 'price', 'for_sale',
                  'old_price', 'size', 'for_order', 'hit_sale',
                  'productalbum']


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор товара."""

    subproduct = SubproductSerializer(many=True)
    size = SizeDoorSerializer(many=True)
    productalbum = serializers.SerializerMethodField()
    productalbumcolor = serializers.SerializerMethodField()

    def get_productalbum(self, obj):
        productalbum = obj.album_product
        serializer = ProductAlbumSerializer(productalbum, many=True)
        return serializer.data

    def get_productalbumcolor(self, obj):
        productalbumcolor = obj.album_color
        serializer = ProductAlbumColorSerializer(productalbumcolor, many=True)
        return serializer.data

    class Meta:
        model = Product
        fields = ['id', 'type', 'category', 'name', 'price', 'for_sale',
                  'old_price', 'subproduct', 'description', 'size',
                  'for_order', 'hit_sale', 'productalbum',
                  'productalbumcolor']


class ArticleSerializer(serializers.ModelSerializer):
    """Сериализатор статей."""

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'date', 'image']


class MinMaxPriceSerializer(serializers.ModelSerializer):
    """Сериализатор максимальной и минимальной цены."""

    min_price = serializers.SerializerMethodField()
    max_price = serializers.SerializerMethodField()

    def get_min_price(self, obj):
        return Product.objects.all().aggregate(Min('price'))['price__min']

    def get_max_price(self, obj):
        return Product.objects.all().aggregate(Max('price'))['price__max']

    class Meta:
        model = Product
        fields = ['min_price', 'max_price']


class RequestForMeasurementSerializer(serializers.ModelSerializer):
    """Сериализатор запроса на замер."""

    class Meta:
        model = RequestForMeasurement
        fields = ['name_surname', 'telefone', 'address', 'content']


class RequestForCallbackSerializer(serializers.ModelSerializer):
    """Сериализатор запроса на замер."""

    class Meta:
        model = RequestForCallback
        fields = ['name_surname', 'telefone']
