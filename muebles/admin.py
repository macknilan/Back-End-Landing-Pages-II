# -*- coding: utf-8 -*-


from django.contrib import admin
from easy_thumbnails.files import get_thumbnailer
from .models import Mueble


@admin.register(Mueble)
class MuebleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'modelo', 'descripcion', 'dimensiones', 'categoria', 'oferta', 'precio', 'foto_uno', 'foto_dos', 'foto_tres', 'foto_cuatro', 'foto_cinco', )
    list_filter = ('modelo', 'categoria', )
    search_fields = ['descripcion', 'modelo', ]
    readonly_fields = ('slug', )
    list_editable = ('modelo', 'descripcion', 'dimensiones', 'categoria', 'oferta', 'precio', )
    # prepopulated_fields = {"slug": ("modelo",)}

    """
    MOSTRAR IMAGENES DEL ADMINISTRADOR
    """
    def foto_uno(self, obj):
        return '<img src="%s">' % get_thumbnailer(obj.foto_1)['img_mueble_admin'].url
    foto_uno.allow_tags = True

    def foto_dos(self, obj):
        return '<img src="%s">' % get_thumbnailer(obj.foto_2)['img_mueble_admin'].url
    foto_dos.allow_tags = True

    def foto_tres(self, obj):
        return '<img src="%s">' % get_thumbnailer(obj.foto_3)['img_mueble_admin'].url
    foto_tres.allow_tags = True

    def foto_cuatro(self, obj):
        return '<img src="%s">' % get_thumbnailer(obj.foto_4)['img_mueble_admin'].url
    foto_cuatro.allow_tags = True

    def foto_cinco(self, obj):
        return '<img src="%s">' % get_thumbnailer(obj.foto_5)['img_mueble_admin'].url
    foto_cinco.allow_tags = True
