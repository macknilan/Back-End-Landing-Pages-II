# -*- coding: utf-8 -*-


from django.contrib import admin
from easy_thumbnails.files import get_thumbnailer
from .models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
#    import ipdb; ipdb.set_trace() # ESTO ES PARA DEBUGEARC
    list_display = ('cat_mueble', 'slug', 'foto_categoria', )
    list_filter = ('cat_mueble', 'slug', )
    search_fields = ['cat_mueble', ]
    readonly_fields = ('slug', )
    # prepopulated_fields = {"slug": ("cat_mueble",)}

    def foto_categoria(self, obj):
        """
        MOSTRAR IMAGENES DEL ADMINISTRADOR
        """
        return '<img src="%s">' % get_thumbnailer(obj.imagen_categoria)['img_categoria_admin'].url
    foto_categoria.allow_tags = True
#    import ipdb; ipdb.set_trace() # ESTO ES PARA DEBUGEARC



