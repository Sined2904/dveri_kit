from rest_framework import serializers

from products.models import (Product, SizeDoor, Article,
                             ProductAlbum, ProductAlbumColor)


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


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор товара."""

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
                  'price_discount', 'subproduct', 'description', 'size',
                  'for_order', 'hit_sale', 'productalbum',
                  'productalbumcolor']


class ArticleSerializer(serializers.ModelSerializer):
    """Сериализатор статей."""

    class Meta:
        model = Article
        fields = ['id', 'title', 'text', 'date']
