# -*- coding: utf-8 -*-

from django import template
from muebles.models import Mueble


register = template.Library()


@register.inclusion_tag('list_mueble_inclusion_tag.html', takes_context=True)
def paginacion_tags_mueble(context):
    """
    FALTA PONER LOS COMENTARIOS
    """
    link_mueble = Mueble.objects.filter(categoria__cat_mueble="comedores").order_by('modelo')
    return {'link_mueble': link_mueble}
