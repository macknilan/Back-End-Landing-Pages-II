# -*- coding: utf-8 -*-


from django.contrib import admin
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.admin import AdminImageMixin
from .models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(AdminImageMixin, admin.ModelAdmin):
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
        return '<img src="%s">' % get_thumbnail(obj.imagen_categoria, '450x450', quality=99).url
    foto_categoria.allow_tags = True
#    import ipdb; ipdb.set_trace() # ESTO ES PARA DEBUGEARC
