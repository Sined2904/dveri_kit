from django.contrib import admin

from .models import Size, Door, DoorAlbum, DoorAlbumColor


class DoorAlbumAdmin(admin.TabularInline):
    model = DoorAlbum


class DoorAlbumColorAdmin(admin.TabularInline):
    model = DoorAlbumColor


class DoorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')
    empty_value_display = '-пусто-'
    search_fields = ('name', )
    ordering = ['name', ]
    inlines = [DoorAlbumAdmin, DoorAlbumColorAdmin]


class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
    empty_value_display = '-пусто-'
    search_fields = ('size', )
    ordering = ['size', ]


admin.site.register(Door, DoorAdmin)
admin.site.register(Size, SizeAdmin)
