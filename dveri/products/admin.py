from django.contrib import admin

from .models import (SizeDoor, Product, ProductAlbum, RequestForCallback,
                     ProductAlbumColor, Article, RequestForMeasurement)


class ProductAlbumAdmin(admin.TabularInline):
    model = ProductAlbum


class ProductAlbumColorAdmin(admin.TabularInline):
    model = ProductAlbumColor


'''
class RelatedProductsAdmin(admin.TabularInline):
    model = RelatedProduct
'''


class ProductAdmin(admin.ModelAdmin):
    list_display = ('type', 'category', 'name',
                    'price', 'for_sale', 'old_price',
                    'for_order', 'hit_sale', 'color_product'
                    )
    empty_value_display = '-пусто-'
    search_fields = ('name',)
    ordering = ['name', ]
    inlines = [ProductAlbumAdmin, ProductAlbumColorAdmin]


class SizeDoorAdmin(admin.ModelAdmin):
    list_display = ('size',)
    empty_value_display = '-пусто-'
    search_fields = ('size', )
    ordering = ['size', ]


class ArticleAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    search_fields = ('title', 'text')
    ordering = ['title', ]


class RequestForMeasurementAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'telefone', 'address',
                    'content', 'time_create'
                    )
    empty_value_display = '-пусто-'
    search_fields = ('name_surname', 'telefone', 'address', 'content')
    ordering = ['-time_create', ]


class RequestForCallbackAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'telefone', 'time_create')
    empty_value_display = '-пусто-'
    search_fields = ('name_surname', 'telefone')
    ordering = ['-time_create', ]


admin.site.register(Product, ProductAdmin)
admin.site.register(SizeDoor, SizeDoorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(RequestForMeasurement, RequestForMeasurementAdmin)
admin.site.register(RequestForCallback, RequestForCallbackAdmin)
