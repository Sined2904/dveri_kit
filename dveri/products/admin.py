from django.contrib import admin

from .models import (SizeDoor, Product, ProductAlbum,
                     ProductAlbumColor)


class ProductAlbumAdmin(admin.TabularInline):
    model = ProductAlbum


class ProductAlbumColorAdmin(admin.TabularInline):
    model = ProductAlbumColor

'''
class RelatedProductsAdmin(admin.TabularInline):
    model = RelatedProduct
'''

class ProductAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]
    inlines = [ProductAlbumAdmin, ProductAlbumColorAdmin]


class SizeDoorAdmin(admin.ModelAdmin):
    list_display = ('size',)
    empty_value_display = '-пусто-'
    search_fields = ('size', )
    ordering = ['size', ]


admin.site.register(Product, ProductAdmin)
admin.site.register(SizeDoor, SizeDoorAdmin)
